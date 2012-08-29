// Generated by CoffeeScript 1.3.3
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  jQuery(function() {
    var FacebookSession, GoogleSession, KibaSession, VkontakteSession;
    KibaSession = (function() {

      function KibaSession() {
        this.first_name = '';
        this.last_name = '';
        this.avatar = '';
        this.id = '';
      }

      KibaSession.initWith = function(resp) {};

      KibaSession.prototype.getFriends = function(callback) {
        return [];
      };

      return KibaSession;

    })();
    GoogleSession = (function(_super) {

      __extends(GoogleSession, _super);

      function GoogleSession() {
        GoogleSession.__super__.constructor.call(this);
      }

      GoogleSession.initWith = function(resp) {
        var name_parts, session;
        name_parts = resp.displayName.split(' ');
        session = new GoogleSession();
        session.first_name = name_parts[0];
        session.last_name = name_parts[1];
        session.avatar = resp.image.url;
        return session;
      };

      return GoogleSession;

    })(KibaSession);
    window.GoogleBackend = (function() {

      function GoogleBackend() {}

      GoogleBackend.scope = 'https://www.googleapis.com/auth/plus.me';

      GoogleBackend.login = function(callback) {
        var that;
        that = this;
        return gapi.auth.authorize({
          client_id: window.GOOGLE_CLIENT_ID,
          scope: GoogleBackend.scope
        }, function(authResult) {
          if (authResult && !authResult.error) {
            return gapi.client.load('plus', 'v1', function() {
              var request;
              request = gapi.client.plus.people.get({
                'userId': 'me'
              });
              return request.execute(function(resp) {
                return callback(GoogleSession.initWith(resp));
              });
            });
          }
        });
      };

      return GoogleBackend;

    })();
    VkontakteSession = (function(_super) {

      __extends(VkontakteSession, _super);

      VkontakteSession.fields = 'uid,first_name,last_name,nickname,sex,bdate,city,country,photo,photo_medium,photo_big';

      function VkontakteSession() {
        VkontakteSession.__super__.constructor.call(this);
      }

      VkontakteSession.initWith = function(resp) {
        var session;
        session = new VkontakteSession();
        session.first_name = resp.user.first_name;
        session.last_name = resp.user.last_name;
        session.id = resp.user.uid;
        return session;
      };

      VkontakteSession.prototype.getFriends = function(callback) {
        return VK.Api.call('friends.get', {
          fields: VkontakteSession.fields
        }, function(r) {
          return callback(r.response);
        });
      };

      return VkontakteSession;

    })(KibaSession);
    window.VkontakteBackend = (function() {

      function VkontakteBackend() {}

      VkontakteBackend.fields = 'city,country,photo,photo_medium,photo_medium_rec,photo_big,photo_rec';

      VkontakteBackend.login = function(callback, settings) {
        if (settings == null) {
          settings = 2;
        }
        return VK.Auth.login(function(response) {
          return VK.Api.call('users.get', {
            uids: response.session.user.id,
            fields: VkontakteBackend.fields
          }, function(r) {
            return callback(VkontakteSession.initWith(response.session));
          });
        }, settings);
      };

      return VkontakteBackend;

    })();
    FacebookSession = (function(_super) {

      __extends(FacebookSession, _super);

      function FacebookSession() {
        FacebookSession.__super__.constructor.call(this);
      }

      FacebookSession.initWith = function(resp) {
        var session;
        session = new FacebookSession();
        session.first_name = resp.first_name;
        session.last_name = resp.last_name;
        return session.id = resp.id;
      };

      FacebookSession.prototype.getFriends = function(callback) {
        return FB.api('/me/friends', function(friends) {
          var friends_mapped, friends_original;
          friends_original = friends.data;
          friends_mapped = $.map(friends_original, function(elementOfArray, indexInArray) {
            var first_name, last_name, name_parts;
            name_parts = elementOfArray.split(' ');
            first_name = '';
            last_name = '';
            if (name_parts.length >= 2) {
              first_name = name_parts[0];
              last_name = name_parts[1];
            } else {
              first_name = elementOfArray.name;
            }
            return {
              id: elementOfArray.id,
              name: elementOfArray.name,
              first_name: first_name,
              last_name: last_name
            };
          });
          return callback(friends_mapped);
        });
      };

      return FacebookSession;

    })(KibaSession);
    return window.FacebookBackend = (function() {

      function FacebookBackend() {}

      FacebookBackend.login = function(callback, scope) {
        if (scope == null) {
          scope = {
            scope: 'email'
          };
        }
        return FB.login(function(response) {
          return FB.api('/me', function(me) {
            return callback(FacebookSession.initWith(me));
          });
        }, scope);
      };

      return FacebookBackend;

    })();
  });

}).call(this);
