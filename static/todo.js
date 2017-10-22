$(document).ready(function(){
    $('#todotable').DataTable({
        "order": [],
        columnDefs: [
            { orderable: false, targets: -1 },
        ],
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search...",
            emptyTable: "You have no to-dos"
        }
    });

    window.onbeforeunload = confirmExit;
    function confirmExit() {
        if (!jQuery.isEmptyObject(json)) {
            return "Todo changes not saved. Do you wish to leave the page?";
        }
    }
});

$('.change-priority').on('change', function() {
    var priority = {};
    priority[this.id] = this.value;

    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(priority),
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

    $(this).parent().attr('data-order', this.value)
    if (this.value == 0 || this.value == 1) {
        $(this).parent().parent().removeClass("table-info table-warning");
    } else if (this.value == 2) {
        $(this).parent().parent().removeClass("table-info table-warning").addClass("table-info");
    } else if (this.value == 3) {
        $(this).parent().parent().removeClass("table-info table-warning").addClass("table-warning");
    }
    $('#todotable').dataTable().api().rows().invalidate('dom').draw();
});


$(function(){
    $("[data-hide]").on("click", function(){
        $(this).closest("." + $(this).attr("data-hide")).fadeOut('fast');
    });
});


$('.remove').on("click", function() {
    var removejson = {};
    removejson[this.value] = -1;
    var tableRow = $(this).closest('tr');
    tableRow.find('td').fadeOut('fast',
        function(){
            tableRow.remove();
        }
    );
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(removejson),
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
