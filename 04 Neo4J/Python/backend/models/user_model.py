from config.db import conn

class User:
    @staticmethod
    def create(username, password):
        query = '''
        CREATE (u:User {username: $username, password: $password})
        RETURN u
        '''
        conn.query(query, parameters={'username': username, 'password': password})

    @staticmethod
    def find_by_username(username):
        query = '''
        MATCH (u:User {username: $username})
        RETURN u
        '''
        result = conn.query(query, parameters={'username': username})
        return result[0]['u'] if result else None

    @staticmethod
    def update_password(username, new_password):
        query = '''
        MATCH (u:User {username: $username})
        SET u.password = $new_password
        RETURN u
        '''
        conn.query(query, parameters={'username': username, 'new_password': new_password})

    @staticmethod
    def delete(username):
        query = '''
        MATCH (u:User {username: $username})
        DELETE u
        '''
        conn.query(query, parameters={'username': username})
