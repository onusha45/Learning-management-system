$(document).ready(function(){
    $('.delete_room').on('click', function(e){
        e.preventDefault();
        const room_id = $(this).data('room-id');
        alert (room_id)
        if(confirm("Do you want to delte this room?")){
            $("#form_delete_"+room_id).submit()
        }
    }
)

})

  