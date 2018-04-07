$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var lineChartData = {
        labels: ['Math', 'Programming 1', 'Data Structure', 'Network', 'Security', 'Software Engineering', 'Computer Vision'],
        datasets: [
            {
                label: 'Pass',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            },
            {
                label: 'Fail',
                label: 'Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                pointBorderColor: '#fff',

                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Pass',
                backgroundColor: 'rgba(234,209,204,0.2)',
                borderColor: 'rgba(234,209,204,1)',
                pointBackgroundColor: 'rgba(234,209,204,1)',

                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Fail',
                backgroundColor: 'rgba(41,54,61,0.2)',
                borderColor: 'rgba(41,54,61,1)',
                pointBackgroundColor: 'rgba(41,54,61,1)',

                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    var chart = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: {
            responsive: true
        }
    });


});
