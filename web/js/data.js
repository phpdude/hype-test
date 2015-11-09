(function($) {
    var apiUrl = 'http://localhost:5000';
    getCookie = function (cname)	{
        var name = cname  +  "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i ++ ) 
          {
          var c = ca[i].trim();
          if (c.indexOf(name)==0) return c.substring(name.length,c.length);
          }
        return "";
    };
    
    var AjaxBase = {
        list:  function(created,failure){
            $.ajax({
                  url:  apiUrl  +  "/"  +  this.entity,
                  method: "GET",
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                  headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
                }).done(function(data){
                    created(data)
                }).fail(function(error){
                    failure(error);
                });
        },
        
        findByRef:  function(ref,created,failure){
            $.ajax({
                  url: apiUrl + "/" + this.entity + "?where=" + JSON.stringify(ref),
                  method: "GET",
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                  headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
                }).done(function(data,method,options){
                    created(data,method,options)
                }).fail(function(error){
                    failure(error);
                });
        },

        create:  function(group,created,failure){
            $.ajax({
                  url: apiUrl + "/" + this.entity,
                  method: "POST",
                  data: JSON.stringify(group),
                  contentType: "application/json; charset=utf-8",
                  headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
                }).done(function(data){
                    created(data)
                }).fail(function(error){
                    if ( failure !== undefined ){
                        failure(error);
                    } else {
                        alert(error._issues[0]);
                    }
                });
        },
        
        update:  function(id,group,updated,failure){
            $.ajax({
                url: apiUrl + "/" + this.entity + "/" + id,
                method: "PATCH",
                data:  JSON.stringify(group),
                contentType: "application/json; charset=utf-8",
                headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
            }).done(function(data){
                updated(data);
            }).fail(function(error){
                failure(error);
            })
        },
        
        remove:  function(id,updated,failure){
            $.ajax({
                url: apiUrl + "/" + this.entity + "/" + id,
                method: "PATCH",
                data:  JSON.stringify({'status': 'archived'}),
                contentType: "application/json; charset=utf-8",
                dataType:  'text',
                headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
            }).done(function(data){
                updated(JSON.parse(data));
            }).fail(function(error){
                faiure(error);
            })
        },
        
    };
    
    
    var Users = {
        entity : 'users',
        getById:  function(id,found,notFoud,failure){
            $.ajax({
                url:  apiUrl + "/users/" + id,
                method:  "GET",
                dataType:  'json',
                headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
            }).done(function (data){
                var result = data;
                found(result);
            }).error(function(error){
                debugger;
                if(error.status == 404)
                    notFound(error);
                else {
                    if(failure)
                        failure(error);
                }
            });
        },
                
        getByVehicle:  function(vehicle_id,created,failure){
            $.ajax({
                  url: apiUrl + "/users?vehicle.nid=" + vehicle_id,
                  method: "GET",
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                  headers :  {'Authorization' :  'Basic ' + btoa(getCookie('username') + ': ' + getCookie('token'))},
                }).done(function(data){
                    created(data)
                }).fail(function(error){
                    failure(error);
                });
        }
    };


   $.extend( Users, AjaxBase );
   
   //this is horrible but fast
   document.Users = Users;
   
   
})(jQuery);