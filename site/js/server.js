var Server = {
    Automaton: {
        create: function( data, callback, error ) {
            $.post( 'api/automaton/create', {
                name: '',
                data: data
            }, function( result ) {
                callback( result.id );
            }, 'json' ).error( function( jqXHR, settings, thrownError ) {
                error( thrownError );
            } );
        },
        view: function( id, callback, error ) {
          // var response = '';
          // $.ajax({
          //   type: "GET",
          //   url: "api/automaton/" + id,
          //   async: false,
          //   success : function(text)
          //       {
          //         response = text;
          //       }, 'json' ).error( function( jqXHR, settings, thrownError ) {
          //           error( thrownError );
          //       });
          //   }
          // return response;
            // $.get( 'api/automaton/' + id, {}, function( result ) {
            //     callback( result );
            // }, 'json' ).error( function( jqXHR, settings, thrownError ) {
            //     error( thrownError );
            // } );
        }
    }
};
