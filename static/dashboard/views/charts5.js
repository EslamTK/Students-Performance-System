$(function () {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 255)
    };

    var data = educatorsRatingData;

    var label_data = [];
    var review_item_label = [];
    var review_item = {};

    for (var i = 0; i < data.length; i++) {
        if (!label_data.includes(data[i].year)) {
            label_data.push(data[i].year);
        }
        if (review_item_label.includes(data[i].review_item__name)) {
            review_item[data[i].review_item__name].push(data[i].rate__avg);
            }
        else {
            review_item_label.push(data[i].review_item__name);
            review_item[data[i].review_item__name] = new Array();
            review_item[data[i].review_item__name].push(data[i].rate__avg);

        }

    }


    var colors = [];
    for (var i = 0; i < review_item_label.length; i++) {
        colors.push('' + randomScalingFactor() + ',' + randomScalingFactor() + ',' + randomScalingFactor() + ',');
    }
    var datasetss = [];
    for (var i = 0; i < review_item_label.length; i++) {
        datasetss.push({
            label: review_item_label[i],
            backgroundColor: 'rgba(' + colors[i] + '0.2)',
            borderColor: 'rgba(' + colors[i] + '1)',
            pointBackgroundColor: 'rgba(' + colors[i] + '1)',
            pointBorderColor: '#fff',
            data: review_item[review_item_label[i]]
        });

    }

    var lineChartData = {
        labels: label_data,
        datasets: datasetss
    }

    var ctx = document.getElementById('canvas-1');
    var chart = new Chart(ctx, {
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


});
