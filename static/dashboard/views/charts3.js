$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 10)
    };

    var my_data = document.getElementById("myVar").value;

    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data);
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);

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
        datasets: [
            {
                label: 'Midterm Pass',
                backgroundColor: 'rgba(144, 164, 174)',
                data: midPass
            },
            {
                label: 'Midterm Fail',
                backgroundColor: 'rgba( 255, 236, 179 )',
                data: midFail
            }
            ,
            {
                label: 'Final Pass',
                backgroundColor: 'rgba( 215, 204, 200 )',
                data: finalPass
            }
            ,
            {
                label: 'Final Fail',
                backgroundColor: 'rgba( 200, 230, 201 )',
                data: finalFail
            }
        ]
    };


    var ctx = document.getElementById('canvas-1');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: lineChartData,
        options: {
            responsive: true,
            beginAtZero: true
        }
    });


});
