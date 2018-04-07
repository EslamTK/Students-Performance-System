$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };
    var lineChartData = {
        labels: ['2001', '2003', '2005', '2007', '2009', '2011', '2013'],
        datasets: [
            {
                label: 'Knowledge',
                backgroundColor: 'rgba(173,220,202,0.2)',
                borderColor: 'rgba(173,220,202,1)',
                pointBackgroundColor: 'rgba(173,220,202,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            },
            {
                label: 'Preparation',
                backgroundColor: 'rgba(220,235,194,0.2)',
                borderColor: 'rgba(220,235,194,1)',
                pointBackgroundColor: 'rgba(220,235,194,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Easy To Follow',
                backgroundColor: 'rgba(254,210,183,0.2)',
                borderColor: 'rgba(254,210,183,1)',
                pointBackgroundColor: 'rgba(254,210,183,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Helpful',
                backgroundColor: 'rgba(239,98,112,0.2)',
                borderColor: 'rgba(239,98,112,1)',
                pointBackgroundColor: 'rgba(239,98,112,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Respectful',
                backgroundColor: 'rgba(244,234,200,0.2)',
                borderColor: 'rgba(244,234,200,1)',
                pointBackgroundColor: 'rgba(244,234,200,1)',
                pointBorderColor: '#fff',
                data: [randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor(), randomScalingFactor()]
            }
            ,
            {
                label: 'Encourage Preparation',
                backgroundColor: 'rgba(33,52,67,0.2)',
                borderColor: 'rgba(33,52,67,1)',
                pointBackgroundColor: 'rgba(33,52,67,1)',
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
