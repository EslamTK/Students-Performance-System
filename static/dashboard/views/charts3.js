var my_data = document.getElementById("myVar").value;

//formating data to valid json format
my_data = my_data.slice(10, my_data.length, my_data);
my_data = my_data.replace('>', '');
my_data = my_data.replace(/'/g, '"');
my_data = JSON.parse(my_data);

window.onload = drawChart(my_data, true);

var selectedYear = "";
var selectedDep = "";
var ter_id = "";
$('#year-selector').change(function () {

    selectedYear = $('#year-selector option:selected').val();
    send_request();


});
$('#department-selector').change(function () {

    selectedDep = $('#department-selector option:selected').val();
    send_request();

});

//function applied on change term 
$("input:radio[name=options]").change(function () {

    ter_id = $('input:radio[name=options]:checked').val();
    send_request();
});

function send_request() {
    'use strict';
    var depId = 'department_id=' + selectedDep + '';
    var yId = '&year_id=' + selectedYear + '';
    var tId = '&term_id=' + ter_id;
    var bUrl = request_url + '?';
    var aUrl = bUrl + depId + yId + tId;

    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            drawChart(data.result);
        }
    });
}


function drawChart(data, isNew) {
    'use strict';

    console.log(data);
    //collecting data
    var label_data = [];
    var midPass = [];
    var midFail = [];
    var finalPass = [];
    var finalFail = [];

    for (var i = 0; i < data.length; i++) {

            label_data.push(data[i].course__name);
            midPass.push(data[i].midterm_pass);
            midFail.push(data[i].total - data[i].midterm_pass);
            finalPass.push(data[i].final_pass);
            finalFail.push(data[i].total - data[i].final_pass);

    }

    var lineChartData = {
        labels: label_data,
        datasets: [{
                label: 'Midterm Pass',
            backgroundColor: 'rgba(220,220,220,0.2)',
            borderColor: 'rgba(220,220,220,1)',
            pointBackgroundColor: 'rgba(220,220,220,1)',
            pointBorderColor: '#fff',
                data: midPass
            },
            {
                label: 'Midterm Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                data: midFail
            },
            {
                label: 'Final Pass',
                backgroundColor: 'rgba(234,209,204,0.2)',
                borderColor: 'rgba(234,209,204,1)',
                pointBackgroundColor: 'rgba(234,209,204,1)',

                pointBorderColor: '#fff',
                data: finalPass
            },
            {
                label: 'Final Fail',
                backgroundColor: 'rgba(41,54,61,0.2)',
                borderColor: 'rgba(41,54,61,1)',
                pointBackgroundColor: 'rgba(41,54,61,1)',

                pointBorderColor: '#fff',
                data: finalFail
            }
        ]
    };

    if (isNew) {
        var ctx = document.getElementById('canvas-1');
        window.chart = new Chart(ctx, {
            type: 'bar',
            data: lineChartData,
            options: {
                responsive: true
            }
        });
    }

    else {
        window.chart.data = lineChartData;
        window.chart.update();
    }
}