var Server = {
    Automaton: {
        create: function( data, callback, error ) {
            $.post( 'api/automaton/create', {
                name: '',
                data: data
            }, function( result ) {
                callback( result );
            }, 'json' ).error( function( jqXHR, settings, thrownError ) {
                error( thrownError );
            } );
        },
        view: function( id, callback, error ) {
            $.get( 'api/automaton/' + id, {}, function( result ) {
                callback( result );
            }, 'json' ).error( function( jqXHR, settings, thrownError ) {
                error( thrownError );
            } );
        }
    },
    Session: {
        view: function() {
          $.ajax({ type: "GET",
                   url: "api/user",
                   async: false,
                   success : function(text)
                     {
                       response = text;
                     }
          });
          return parseInt(response);
        },
        user: function(gid) {
          $.ajax({ type: "GET",
                   url: "api/user/" + gid,
                   async: false,
                   success : function(text)
                     {
                       response = text;
                     }
          });
          return response
        },
        user_automata: function(gid) {
          $.ajax({ type: "GET",
                   url: "api/user/" + gid + "/automata",
                   async: false,
                   success : function(text)
                     {
                       response = text;
                     }
          });
          return JSON.parse(response)
        }
    }
};
