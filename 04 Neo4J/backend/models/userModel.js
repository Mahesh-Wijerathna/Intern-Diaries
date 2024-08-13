class User {
    constructor(username, password) {
      this.username = username;
      this.password = password;
    }
  
    static async create(username, password) {
      const session = require('../config/db').session;
      const result = await session.run(
        'CREATE (u:User {username: $username, password: $password}) RETURN u',
        { username, password }
      );
      return result.records[0].get('u');
    }
  
    static async findByUsername(username) {
      const session = require('../config/db').session;
      const result = await session.run(
        'MATCH (u:User {username: $username}) RETURN u',
        { username }
      );
      return result.records.length > 0 ? result.records[0].get('u') : null;
    }
  
    static async updatePassword(username, newPassword) {
      const session = require('../config/db').session;
      const result = await session.run(
        'MATCH (u:User {username: $username}) SET u.password = $newPassword RETURN u',
        { username, newPassword }
      );
      return result.records[0].get('u');
    }
  
    static async delete(username) {
      const session = require('../config/db').session;
      await session.run(
        'MATCH (u:User {username: $username}) DELETE u',
        { username }
      );
    }
  }
  
  module.exports = User;
  