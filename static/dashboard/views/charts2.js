$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var lineChartData = {
        labels: ['Knowledge', 'Preparation', 'Easy To Follow', 'Helpful', 'Respectful', 'Encourage Participation'],
        datasets: [
            {
                label: 'Rate',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            },

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
