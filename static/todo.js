var json = {};

$(document).ready(function(){
    $('#todotable').DataTable({
        "order": [[3, "asc"], [4, "desc"]],
        columnDefs: [
            { orderable: false, targets: -1 },
        ],
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search...",
            emptyTable: "You have no to-dos"
        }
    });
});

$('select').on('change', function() {
    $(this).parent().attr('data-order', this.value)
    if (this.value == 0 || this.value == 1) {
        $(this).parent().parent().removeClass("table-info table-warning");
    } else if (this.value == 2) {
        $(this).parent().parent().removeClass("table-info table-warning").addClass("table-info");
    } else if (this.value == 3) {
        $(this).parent().parent().removeClass("table-info table-warning").addClass("table-warning");
    }
    $('#todotable').dataTable().api().rows().invalidate('dom').draw();
    json[this.id] = this.value;
});

$('#update').click(function() {
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(json),
        url: '/todo/update',
        dataType: 'json',
        success: function (e) {
            $('#failure').fadeOut('fast');
            $('#success').fadeTo(500,1);
        },
        error: function(e) {
            $('#success').fadeOut('fast');
            $('#failure').fadeTo(500,1);
        }
    });

});

$(function(){
    $("[data-hide]").on("click", function(){
        $(this).closest("." + $(this).attr("data-hide")).fadeOut('fast');
    });
});