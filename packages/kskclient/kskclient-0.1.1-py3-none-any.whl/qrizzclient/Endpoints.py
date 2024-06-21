class Endpoints:
    def __init__(self):
        self.auth_endpoints = {
            'create_user': 'auth/createuser',
            'login': 'auth/login',
            'get_user': 'auth/getuser'
        }

        self.chat_endpoints = {
            'search': 'chat/store',
            'new_conv': 'chat/newConv',
            'get_user_conv': 'chat/getUserConv',
            'get_conv': 'chat/getConv',
            'get_title': 'chat/getTitle',
            'set_title': 'chat/setTitle',
            'pin_msg': 'chat/pin',
            'regenerate_msg': 'chat/regenerate',
            'get_fav_queries': 'chat/getFavQueries',
            'get_fav_charts': 'chat/getFavCharts',
            'unpin_msg': 'chat/unpin',
            'clear_conv': 'chat/clear'
        }

        self.connectdb_endpoints = {
            'store_db': 'connectdb/storedb',
            'store_schema': 'connectdb/storeschema',
            'get_schema': 'connectdb/getschema',
            'submit_cred': 'connectdb/submitcred',
            'get_db': 'connectdb/getdb',
            'delete_db': 'connectdb/deletedb'
        }

        self.file_endpoints = {
            'upload_file': 'upload',
            'store_schema':'storeschema',
            'get_schema':"getschema",
            'get_files': 'get-files',
            'get_all_files': 'get-all-files',
            'delete_file': 'deletefile',
            'update_file': 'updatefile'
        }