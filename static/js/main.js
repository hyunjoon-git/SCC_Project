$(document).ready(function () {

    $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex){
            var min = Date.parse($('#fromDate').val());
            var max = Date.parse($('#toDate').val());
            var targetDate = Date.parse(data[1]);

            if( (isNaN(min) && isNaN(max) ) || 
                (isNaN(min) && targetDate <= max )|| 
                ( min <= targetDate && isNaN(max) ) ||
                ( targetDate >= min && targetDate <= max) ){ 
                    return true;
            }
            return false;
        }
    )

    var table = $('#myTable').DataTable({
        ajax: {
            'url':'/post',
            'type': 'GET',
            'dataSrc':''
        },
        responsive: true,
        orderMulti: true,
        order : [[1, 'desc']],
        columnDefs: [
            {
                orderable: false,
                className: 'select-checkbox',
                targets: 0
            },
            {
                data: 'date',
                targets: 1
            },
            {
                data: 'title',
                targets: 2
            },
            {
                // The `data` parameter refers to the data for the cell (defined by the
                // `data` option, which defaults to the column being worked with, in
                // this case `data: 0`.

                targets: 3,
                data: "link",
                render: function ( data, type, row ) {
                    return '<a href="'+data+'">Link</a>';
                },
            }
        ],
        select: {
            style:    'os',
            selector: 'td:first-child'
        },
        dom : 'Blfrtip',
        buttons:[{
			extend:'csvHtml5',
			text: 'Export CSV',
			footer: true,
			bom: true,
			className: 'exportCSV'
		}]
    });

    /* Column별 검색기능 추가 */
    $('#myTable_filter').prepend('<select id="select"></select>');
    $('#myTable > thead > tr').children().each(function (indexInArray, valueOfElement) { 
        $('#select').append('<option>'+valueOfElement.innerHTML+'</option>');
    });
    
    $('.dataTables_filter input').unbind().bind('keyup', function () {
        var colIndex = document.querySelector('#select').selectedIndex;
        table.column(colIndex).search(this.value).draw();
    });

    /* 날짜검색 이벤트 리바인딩 */
    $('#myTable_filter').prepend('<input type="text" id="toDate" placeholder="yyyy-MM-dd"> ');
    $('#myTable_filter').prepend('<input type="text" id="fromDate" placeholder="yyyy-MM-dd">~');
    $('#toDate, #fromDate').unbind().bind('keyup',function(){
        table.draw();
    })


});