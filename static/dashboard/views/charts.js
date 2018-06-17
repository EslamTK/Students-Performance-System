var my_data = document.getElementById("myVar").value;
var prediction_data = true;
//transform string into valid json string
var my_data = my_data.replace(/'/g, '"');

//trasnform data into json
defaultData = JSON.parse(my_data);
window.onload = drawChart(defaultData, true);
var selectedYear = "";
var ter_id = "";

$('#year-selector').change(function () {

    selectedYear = $('#year-selector option:selected').val();
    send_request();
});


$("input:radio[name=options]").change(function () {

    ter_id = $('input[name=options]:checked').val();
    send_request();
});


function send_request() {
    'use strict';
    console.log("selectedYear: " + selectedYear);
    var yId = '?year_id=' + selectedYear;
    var tId = '&term_id=' + ter_id;
    var bUrl = request_url;
    var aUrl = bUrl + yId + tId;
    console.log(aUrl);
    console.log("URL: " + aUrl);

    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            prediction_data = false;
            drawChart(data.result);
        }
    });
}

function drawChart(data, isNew) {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    console.log("bam");
    console.log(data);

    //collecting data
    var label_data = [];
    var midterm = [];
    var prediction = [];
    for (var i = 0; i < data.length; i++) {
        label_data.push(data[i].name);
        midterm.push(data[i].midterm);
        if (prediction_data === true)
            prediction.push(data[i].prediction);
        else
            prediction.push(data[i].final);

    }
    var lineChartData = {
        labels: label_data,
        datasets: [{
            label: 'MidTerm',
            backgroundColor: 'rgba(220,220,220,0.2)',
            borderColor: 'rgba(220,220,220,1)',
            pointBackgroundColor: 'rgba(220,220,220,1)',
            pointBorderColor: '#fff',
            data: midterm
        },
            {
                label: 'Expected Final Grades',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: prediction
            }
        ]
    };

    if (isNew) {
        var ctx = document.getElementById('canvas-1');
        window.chart = new Chart(ctx, {
            type: 'bar',
            data: lineChartData,
            options: {
                responsive: true,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    }
    else {
        window.chart.data = lineChartData;
        window.chart.update();
    }

}