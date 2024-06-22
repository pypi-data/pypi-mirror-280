import re
from kabaret import flow
from kabaret.app.ui.gui.icons import gui as _
from kabaret.flow_entities.entities import Property
from libreflow.baseflow.asset import (
    Asset               as BaseAsset,
    AssetFamily         as BaseAssetFamily,
    AssetType           as BaseAssetType,
    AssetTypeCollection as BaseAssetTypeCollection,
    AssetLibrary        as BaseAssetLibrary,
    AssetLibraryCollection as BaseAssetLibraryCollection,
    AssetCollection
)

from .task import Tasks


class Asset(BaseAsset):
    
    tasks = flow.Child(Tasks).ui(expanded=True)

    def ensure_tasks(self):
        """
        Creates the tasks of this asset based on the task
        templates of the project, skipping any existing task.
        """
        mgr = self.root().project().get_task_manager()

        for dt in mgr.get_default_tasks(template_name='asset', exclude_optional=True, entity_oid=self.oid()):
            if not self.tasks.has_mapped_name(dt.name()):
                t = self.tasks.add(dt.name())
                t.enabled.set(dt.enabled.get())
        
        self.tasks.touch()
    
    def _fill_ui(self, ui):
        ui['custom_page'] = 'libreflow.baseflow.ui.task.TasksCustomWidget'


class CreateKitsuAssets(flow.Action):

    ICON = ('icons.libreflow', 'kitsu')

    skip_existing = flow.SessionParam(False).ui(editor='bool')
    create_task_default_files = flow.SessionParam(True).ui(editor='bool')

    _asset_lib = flow.Parent(4)
    _asset_type = flow.Parent(2)
    _assets = flow.Parent()

    def allow_context(self, context):
        return context

    def get_buttons(self):
        return ['Create assets', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        session = self.root().session()
        
        skip_existing = self.skip_existing.get()
        kitsu_api = self.root().project().kitsu_api()
        episode_name = self._asset_lib.kitsu_name.get()
        if episode_name == 'MAIN_PACK':
            episode_name = 'default_episode'
        assets_data = kitsu_api.get_assets_data(self._asset_type.kitsu_name.get(), episode_name)

        for data in assets_data:
            kitsu_name = data['name']
            name = re.sub(r'[\s.-]', '_', kitsu_name)

            if not self._assets.has_mapped_name(name):
                session.log_info(f'[Create Kitsu Assets] Creating Asset {name}')
                a = self._assets.add(name)
            elif not skip_existing:
                a = self._assets[name]
                session.log_info(f'[Create Kitsu Assets] Updating Default Tasks {name}')
                a.ensure_tasks()
            else:
                continue
            
            a.display_name.set(kitsu_name)
            a.code.set(name)

            if self.create_task_default_files.get():
                for t in a.tasks.mapped_items():
                    session.log_info(f'[Create Kitsu Assets] Updating Default Files {name} {t.name()}')
                    t.create_dft_files.files.update()
                    t.create_dft_files.run(None)
        
        self._assets.touch()


class Assets(AssetCollection):

    create_assets = flow.Child(CreateKitsuAssets)

    def add(self, name, object_type=None):
        a = super(Assets, self).add(name, object_type)
        a.ensure_tasks()
        
        return a


class AssetFamily(BaseAssetFamily):
    
    assets = flow.Child(Assets).ui(expanded=True, show_filter=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            edits = super(AssetFamily, self).get_default_contextual_edits(context_name)
            edits['path_format'] = 'lib/{asset_type}/{asset_family}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            return edits


class AssetType(BaseAssetType):
    
    kitsu_name = Property().ui(hidden=True, editable=False)
    assets = flow.Child(Assets).ui(expanded=True, show_filter=True)
    asset_families = flow.Child(flow.Object).ui(hidden=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            edits = super(AssetType, self).get_default_contextual_edits(context_name)
            edits['path_format'] = 'lib/{asset_type}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            return edits


class ToggleKitsuAssetType(flow.Action):

    _asset_type = flow.Parent()

    def needs_dialog(self):
        return False
    
    def run(self, button):
        self._asset_type.enabled.set(
            not self._asset_type.enabled.get())
        self._asset_type.touch()


class EditKitsuAssetType(flow.Action):

    display_name = flow.SessionParam()
    code = flow.SessionParam()
    _asset_type = flow.Parent()
    _map = flow.Parent(2)

    def needs_dialog(self):
        self.display_name.set(self._asset_type.display_name.get())
        self.code.set(self._asset_type.code.get())
        return True
    
    def get_buttons(self):
        return ['Save', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        self._asset_type.display_name.set(self.display_name.get())
        self._asset_type.code.set(self.code.get())
        self._map.touch()


class RefreshKitsuMap(flow.Action):
    
    ICON = ('icons.libreflow', 'refresh')

    _map = flow.Parent()

    def needs_dialog(self):
        return False
    
    def run(self, button):
        self._map.refresh()


class KitsuAssetType(flow.SessionObject):

    type_name = flow.Param()
    display_name = flow.Param()
    code = flow.Param()
    kitsu_name = flow.Param()
    enabled = flow.BoolParam(True)
    exists = flow.BoolParam(False)

    edit = flow.Child(EditKitsuAssetType)
    toggle = flow.Child(ToggleKitsuAssetType)


class KitsuAssetTypes(flow.DynamicMap):

    ICON = ('icons.libreflow', 'kitsu')

    refresh_action = flow.Child(RefreshKitsuMap).ui(label='Refresh')
    _action = flow.Parent()
    _asset_types = flow.Parent(2)
    _asset_lib = flow.Parent(3)

    @classmethod
    def mapped_type(cls):
        return KitsuAssetType
    
    def __init__(self, parent, name):
        super(KitsuAssetTypes, self).__init__(parent, name)
        self._cache = None
        self._names = None
    
    def mapped_names(self, page_num=0, page_size=None):
        if self._cache is None:
            self._mng.children.clear()

            i = 0
            self._cache = {}
            self._names = []

            episode_name = self._asset_lib.kitsu_name.get()
            if episode_name == 'MAIN_PACK':
                episode_name = 'default_episode'
            kitsu_api = self.root().project().kitsu_api()
            assets_data = kitsu_api.get_assets_data(episode_name=episode_name)
            existing_types = self._asset_types.mapped_names()
            
            # Retrieve the list of types from assets of the current episode
            kitsu_names = set()
            for data in assets_data:
                if data['name'] == 'x':
                    continue
                kitsu_names.add(kitsu_api.get_asset_type(data)['name'])
            
            for kitsu_name in sorted(kitsu_names):
                mapped_name = f'at{i:04}'
                name = re.sub(r'[\s.-]', '_', kitsu_name)
                self._names.append(mapped_name)
                self._cache[mapped_name] = dict(
                    name=name,
                    display_name=kitsu_name, # use Kitsu name as display name
                    code=name,
                    kitsu_name=kitsu_name,
                    exists=name in existing_types
                )
                i += 1
        
        # Remove asset libs from list if `skip_existing` is true
        names = self._names
        if self._action.skip_existing.get():
            names = [
                n for n in names
                if not self._cache[n]['exists']
            ]
        
        return names

    def columns(self):
        return ['Name', 'Display name', 'Code']
    
    def refresh(self):
        self._cache = None
        self.touch()

    def _configure_child(self, child):
        self.mapped_names()
        child.type_name.set(self._cache[child.name()]['name'])
        child.display_name.set(self._cache[child.name()]['display_name'])
        child.code.set(self._cache[child.name()]['code'])
        child.kitsu_name.set(self._cache[child.name()]['kitsu_name'])
        child.exists.set(self._cache[child.name()]['exists'])
    
    def _fill_row_cells(self, row, item):
        row['Name'] = item.type_name.get()
        row['Display name'] = item.display_name.get()
        row['Code'] = item.code.get()
    
    def _fill_row_style(self, style, item, row):
        style['Name_activate_oid'] = item.toggle.oid()
        style['Display name_activate_oid'] = item.edit.oid()
        style['Code_activate_oid'] = item.edit.oid()
        style['icon'] = ('icons.gui',
            'check' if item.enabled.get() else 'check-box-empty')

        if item.exists.get():
            for col in self.columns():
                style[f'{col}_foreground_color'] = '#4e5255'


class CreateKitsuAssetTypes(flow.Action):

    ICON = ('icons.libreflow', 'kitsu')

    kitsu_asset_types = flow.Child(KitsuAssetTypes).ui(expanded=True)
    
    select_all = flow.SessionParam(True).ui(editor='bool').watched()
    skip_existing = flow.SessionParam(False).ui(editor='bool').watched()
    create_assets = flow.SessionParam(False).ui(editor='bool')
    create_task_default_files = flow.SessionParam(False).ui(editor='bool')
    
    _asset_types = flow.Parent()
    _asset_lib = flow.Parent(2)

    def needs_dialog(self):
        self.kitsu_asset_types.refresh()
        self.select_all.set_watched(False)
        self.select_all.revert_to_default()
        self.select_all.set_watched(True)
        return True

    def allow_context(self, context):
        return context
    
    def get_buttons(self):
        return ['Create asset types', 'Cancel']
    
    def child_value_changed(self, child_value):
        if child_value is self.skip_existing:
            self.kitsu_asset_types.touch()
        elif child_value is self.select_all:
            select_all = self.select_all.get()
            for at in self.kitsu_asset_types.mapped_items():
                at.enabled.set(select_all)
            self.kitsu_asset_types.touch()
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        session = self.root().session()

        create_assets = self.create_assets.get()
        skip_existing = self.skip_existing.get()

        for kitsu_at in self.kitsu_asset_types.mapped_items():
            if not kitsu_at.enabled.get():
                continue
            
            name = kitsu_at.type_name.get()

            if not self._asset_types.has_mapped_name(name):
                session.log_info(f'[Create Kitsu Asset Types] Creating Asset Type {name}')
                at = self._asset_types.add(name)
            elif not skip_existing:
                session.log_info(f'[Create Kitsu Asset Types] Asset Type {name} exists')
                at = self._asset_types[name]
            else:
                continue

            at.display_name.set(kitsu_at.display_name.get())
            at.code.set(kitsu_at.code.get())
            at.kitsu_name.set(kitsu_at.kitsu_name.get())

            if create_assets:
                at.assets.create_assets.skip_existing.set(skip_existing)
                at.assets.create_assets.create_task_default_files.set(self.create_task_default_files.get())
                at.assets.create_assets.run('Create assets')
        
        self._asset_types.touch()


class AssetTypeCollection(BaseAssetTypeCollection):

    create_asset_types = flow.Child(CreateKitsuAssetTypes)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                path_format='lib/{asset_type}/{asset_family}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            )


class AssetLibrary(BaseAssetLibrary):

    kitsu_name = Property().ui(hidden=True, editable=False)
    asset_types = flow.Child(AssetTypeCollection).ui(expanded=True)


class ToggleKitsuAssetLib(flow.Action):

    _asset_lib = flow.Parent()

    def needs_dialog(self):
        return False
    
    def run(self, button):
        self._asset_lib.enabled.set(
            not self._asset_lib.enabled.get())
        self._asset_lib.touch()


class EditKitsuAssetLib(flow.Action):

    display_name = flow.SessionParam()
    code = flow.SessionParam()
    _asset_lib = flow.Parent()
    _map = flow.Parent(2)

    def needs_dialog(self):
        self.display_name.set(self._asset_lib.display_name.get())
        self.code.set(self._asset_lib.code.get())
        return True
    
    def get_buttons(self):
        return ['Save', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return
        
        self._asset_lib.display_name.set(self.display_name.get())
        self._asset_lib.code.set(self.code.get())
        self._map.touch()


class KitsuAssetLib(flow.SessionObject):

    lib_name = flow.Param()
    display_name = flow.Param()
    code = flow.Param()
    kitsu_name = flow.Param()
    enabled = flow.BoolParam(True)
    exists = flow.BoolParam(False)

    edit = flow.Child(EditKitsuAssetLib)
    toggle = flow.Child(ToggleKitsuAssetLib)


class KitsuAssetLibs(flow.DynamicMap):

    ICON = ('icons.libreflow', 'kitsu')

    refresh_action = flow.Child(RefreshKitsuMap).ui(label='Refresh')
    _action = flow.Parent()
    _asset_libs = flow.Parent(2)

    @classmethod
    def mapped_type(cls):
        return KitsuAssetLib
    
    def __init__(self, parent, name):
        super(KitsuAssetLibs, self).__init__(parent, name)
        self._cache = None
        self._names = None
    
    def mapped_names(self, page_num=0, page_size=None):
        if self._cache is None:
            self._mng.children.clear()

            i = 0
            self._cache = {}
            self._names = []
            episodes_data = self.root().project().kitsu_api().get_episodes_data()
            existing_libs = self._asset_libs.mapped_names()

            for episode in episodes_data:
                name = episode['name']

                if name == 'x':
                    continue
                
                mapped_name = f'al{i:04}'
                kitsu_name = name
                name = re.sub(r'[\s.-]', '_', name)
                self._names.append(mapped_name)
                self._cache[mapped_name] = dict(
                    name=name,
                    display_name=kitsu_name, # use Kitsu name as display name
                    code=name,
                    kitsu_name=kitsu_name,
                    exists=name in existing_libs
                )
                i += 1
            
            self._names.append(f'al{i:04}')
            self._cache[f'al{i:04}'] = dict(
                name='MAIN_PACK',
                display_name='MAIN_PACK',
                code='MP',
                kitsu_name='MAIN_PACK',
                exists='MAIN_PACK' in existing_libs
            )
        
        # Remove asset libs from list if `skip_existing` is true
        names = self._names
        if self._action.skip_existing.get():
            names = [
                n for n in names
                if not self._cache[n]['exists']
            ]
        
        return names

    def columns(self):
        return ['Name', 'Display name', 'Code']
    
    def refresh(self):
        self._cache = None
        self.touch()

    def _configure_child(self, child):
        self.mapped_names()
        child.lib_name.set(self._cache[child.name()]['name'])
        child.display_name.set(self._cache[child.name()]['display_name'])
        child.code.set(self._cache[child.name()]['code'])
        child.kitsu_name.set(self._cache[child.name()]['kitsu_name'])
        child.exists.set(self._cache[child.name()]['exists'])
    
    def _fill_row_cells(self, row, item):
        row['Name'] = item.lib_name.get()
        row['Display name'] = item.display_name.get()
        row['Code'] = item.code.get()
    
    def _fill_row_style(self, style, item, row):
        style['Name_activate_oid'] = item.toggle.oid()
        style['Display name_activate_oid'] = item.edit.oid()
        style['Code_activate_oid'] = item.edit.oid()
        style['icon'] = ('icons.gui',
            'check' if item.enabled.get() else 'check-box-empty')

        if item.exists.get():
            for col in self.columns():
                style[f'{col}_foreground_color'] = '#4e5255'


class CreateKitsuAssetLibs(flow.Action):
    '''
    When `create_assets` is enabled, the action creates types and assets
    all at once.
    '''
    
    ICON = ('icons.libreflow', 'kitsu')

    kitsu_asset_libs = flow.Child(KitsuAssetLibs).ui(expanded=True)

    skip_existing = flow.SessionParam(False).ui(editor='bool').watched()
    select_all = flow.SessionParam(True).ui(editor='bool').watched()
    create_asset_types = flow.SessionParam(False).ui(editor='bool')
    create_assets = flow.SessionParam(False).ui(editor='bool')

    _asset_libs = flow.Parent()

    def needs_dialog(self):
        self.kitsu_asset_libs.refresh()
        self.select_all.set_watched(False)
        self.select_all.revert_to_default()
        self.select_all.set_watched(True)
        return True

    def allow_context(self, context):
        return context

    def get_buttons(self):
        return ['Create libraries', 'Cancel']
    
    def child_value_changed(self, child_value):
        if child_value is self.skip_existing:
            self.kitsu_asset_libs.touch()
        elif child_value is self.select_all:
            select_all = self.select_all.get()
            for al in self.kitsu_asset_libs.mapped_items():
                al.enabled.set(select_all)
            self.kitsu_asset_libs.touch()
    
    def run(self, button):
        if button == 'Cancel':
            return

        session = self.root().session()
        
        create_asset_types = self.create_asset_types.get()
        create_assets = self.create_assets.get()
        skip_existing = self.skip_existing.get()

        for kitsu_al in self.kitsu_asset_libs.mapped_items():
            if not kitsu_al.enabled.get():
                continue
            
            name = kitsu_al.lib_name.get()

            if not self._asset_libs.has_mapped_name(name):
                session.log_info(f'[Create Kitsu Asset Libs] Creating Asset Library {name}')
                al = self._asset_libs.add(name)
            elif not skip_existing:
                session.log_info(f'[Create Kitsu Asset Libs] Asset Library {name} exists')
                al = self._asset_libs[name]
            else:
                continue

            al.display_name.set(kitsu_al.display_name.get())
            al.code.set(kitsu_al.code.get())
            al.kitsu_name.set(kitsu_al.kitsu_name.get())

            if create_asset_types:
                al.asset_types.create_asset_types.skip_existing.set(skip_existing)
                if create_assets:
                    al.asset_types.create_asset_types.create_assets.set(create_assets)
                al.asset_types.create_asset_types.run('Create asset types')
        
        self._asset_libs.touch()


class AssetLibraryCollection(BaseAssetLibraryCollection):
    
    create_libs = flow.Child(CreateKitsuAssetLibs).ui(label='Create asset libraries')
