from kabaret import flow
from libreflow.baseflow.asset import (
    Asset               as BaseAsset,
    AssetFamily         as BaseAssetFamily,
    AssetType           as BaseAssetType,
    AssetTypeCollection as BaseAssetTypeCollection,
    AssetCollection
)

from .task import Tasks


class Asset(BaseAsset):
    
    tasks = flow.Child(Tasks).ui(expanded=True)

    def ensure_tasks(self):
        """
        Creates the tasks of this asset based on the default
        tasks created with a template named `asset`, skipping
        any existing task.
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
        assets_data = self.root().project().kitsu_api().get_assets_data(self._asset_type.name())
        for data in assets_data:
            name = data['name']

            if not self._assets.has_mapped_name(name):
                session.log_info(f'[Create Kitsu Assets] Creating Asset {name}')
                a = self._assets.add(name)
            elif not skip_existing:
                a = self._assets[name]
                session.log_info(f'[Create Kitsu Assets] Updating Default Tasks {name}')
                a.ensure_tasks()
            else:
                continue

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
    
    assets = flow.Child(Assets).ui(expanded=True, show_filter=True, default_height=600)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            edits = super(AssetFamily, self).get_default_contextual_edits(context_name)
            edits['path_format'] = 'lib/{asset_type}/{asset_family}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            return edits


class AssetType(BaseAssetType):
    
    assets = flow.Child(Assets).ui(expanded=True, show_filter=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            edits = super(AssetType, self).get_default_contextual_edits(context_name)
            edits['path_format'] = 'lib/{asset_type}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            return edits


class AssetModules(AssetType):
    
    asset_families = flow.Child(flow.Object).ui(hidden=True)

    assets = flow.Child(Assets).ui(expanded=True)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                path_format='lib/{asset_type}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            )


class CreateKitsuAssetTypes(flow.Action):

    ICON = ('icons.libreflow', 'kitsu')

    skip_existing = flow.SessionParam(False).ui(editor='bool')
    create_assets = flow.SessionParam(False).ui(editor='bool')
    create_task_default_files = flow.SessionParam(False).ui(editor='bool')

    _asset_types = flow.Parent()

    def get_buttons(self):
        return ['Create asset types', 'Cancel']
    
    def run(self, button):
        if button == 'Cancel':
            return

        session = self.root().session()
        
        asset_types_data = self.root().project().kitsu_api().get_asset_types_data()
        create_assets = self.create_assets.get()
        skip_existing = self.skip_existing.get()

        for data in asset_types_data:
            name = data['name']

            if name == 'x':
                continue

            if not self._asset_types.has_mapped_name(name):
                session.log_info(f'[Create Kitsu Asset Types] Creating Asset Type {name}')
                a = self._asset_types.add(name)
            elif not skip_existing:
                session.log_info(f'[Create Kitsu Asset Types] Asset Type {name} exists')
                a = self._asset_types[name]
            else:
                continue
            
            if create_assets:
                a.assets.create_assets.skip_existing.set(skip_existing)
                a.assets.create_assets.create_task_default_files.set(self.create_task_default_files.get())
                a.assets.create_assets.run('Create assets')
        
        self._asset_types.touch()


class AssetTypeCollection(BaseAssetTypeCollection):

    create_asset_types = flow.Child(CreateKitsuAssetTypes)

    def get_default_contextual_edits(self, context_name):
        if context_name == 'settings':
            return dict(
                path_format='lib/{asset_type}/{asset_family}/{asset}/{task}/{file}/{revision}/{asset}_{file_base_name}'
            )
