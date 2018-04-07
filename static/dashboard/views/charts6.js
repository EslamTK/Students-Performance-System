$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var lineChartData = {
        labels: ['Knowledge', 'Preparation', 'Easy To Follow', 'Helpful', 'Respectful', 'Encourage'],
        datasets: [
            {
                label: 'Encourage Preparation',
                backgroundColor: 'rgba(33,52,67,0.2)',
                borderColor: 'rgba(33,52,67,1)',
                pointBackgroundColor: 'rgba(33,52,67,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
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
