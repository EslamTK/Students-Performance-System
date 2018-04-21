$(function () {
    'use strict';
    $.ajax({
        url: 'http://127.0.0.1:8000/dashboard/administrator_educators_rating',
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        data: data,
        success: function (data) {
            var label_data = [];   //year
            var review_item_label = []; // item_name
            var review_item = {};

            for (var i = 0; i < data.result.length; i++) {
                if (!label_data.includes(data.result[i].year)) {
                    label_data.push(data.result[i].year);
                }
                if (review_item_label.includes(data.result[i].review_item__name)) {
                    review_item[data.result[i].review_item__name].push(data.result[i].rate__avg);
                    }
                else {
                    review_item_label.push(data.result[i].review_item__name);
                    review_item[data.result[i].review_item__name] = new Array();
                    review_item[data.result[i].review_item__name].push(data.result[i].rate__avg);

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

            var barChartData = {
                labels: label_data,
                datasets: datasetss
            }

            var ctx = document.getElementById('canvas-1');
            var chart = new Chart(ctx, {
                type: 'bar',
                data: barChartData,
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
    });

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 255)
    };

    var data = educatorsRatingData;
});
