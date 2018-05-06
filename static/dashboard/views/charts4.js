window.onload = default_;
var selectedYear="";
var selectedDep="";
var ter_id="";
window.selected_year = null;
window.selected_dep = null;
$('#year-selector').change(function () {
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    selectedYear = $('#year-selector option:selected').val();
    send_request();
});
$('#department-selector').change(function () {
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    selectedDep = $('#department-selector option:selected').val();
    send_request();
});

//function applied on change term 
$("input:radio[name=options]").change(function () {
    // erase old data from chart when update data 
    if (window.chart !== undefined || window.chart !== null) {
        window.chart.destroy();
    }
    var ter_id = $('input:radio[name=options]:checked').val();
    send_request();
});

function send_request() {
    'use strict';
    console.log("selectedYear: " + selectedYear);
    console.log("selectedDep: " + selectedDep);
    var depId = 'department_id=' + selectedDep + '';
    var yId = '&year=' + selectedYear + '';
    var tId = '&term_id=' + ter_id + '';
    var bUrl = request_url + '?';
    var aUrl;
    aUrl = bUrl + depId + yId + tId;

    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            var label_data = [];
            var success = [];
            var fail = [];


            for (var i = 0; i < data.result.length; i++) {

                label_data.push(data.result[i].year);
                success.push(data.result[i].success);
                fail.push(data.result[i].fail);
                console.log(data.result[i].year);
                console.log(data.result[i].success);
                console.log(data.result[i].fail);
            }
            /////////
            var lineChartData = {
                labels: label_data,
                datasets: [{
                        label: 'success',
                        backgroundColor: 'rgba(220,220,220,0.2)',
                        borderColor: 'rgba(220,220,220,1)',
                        pointBackgroundColor: 'rgba(220,220,220,1)',
                        pointBorderColor: '#fff',
                        data: success
                    },
                    {
                        label: 'Fail',
                        backgroundColor: 'rgba(151,187,205,0.2)',
                        borderColor: 'rgba(151,187,205,1)',
                        pointBackgroundColor: 'rgba(151,187,205,1)',
                        pointBorderColor: '#fff',
                        data: fail
                    }
                ]
            }


            var ctx = document.getElementById('canvas-1');
            window.chart = new Chart(ctx, {
                type: 'bar',
                data: lineChartData,
                options: {
                    scales: {
                        yAxes: [{
                            display: true,
                            ticks: {
                                beginAtZero: true,
                                stepSize: 0.2,
                                max: 2
                            }
                        }]
                    },
                    responsive: true
                }
            });
            ///////////
        }
    });
}

function default_() {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };

    //getting data from hidden input field
    var my_data = document.getElementById("myData").value;
    console.log("bam");
    console.log(my_data);
    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);
    console.log(data);

    var label_data = [];
    var success = [];
    var fail = [];


    for (var i = 0; i < data.length; i++) {

        label_data.push(data[i].year);
        success.push(data[i].success);
        fail.push(data[i].fail);
    }
    console.log(success);
    var lineChartData = {
        labels: label_data,
        datasets: [{
                label: 'success',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: success
            },
            {
                label: 'Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: fail
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    window.chart = new Chart(ctx, {
        type: 'bar',
        data: lineChartData,
        options: {
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 10
                    }
                }]
            }
        }
    });


}