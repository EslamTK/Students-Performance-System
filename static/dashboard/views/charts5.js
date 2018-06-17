var my_data = educatorsRatingData;

window.onload = drawChart(my_data, true);
var selectedDep = "";
var selectedYear = "";
$('#year-selector').change(function () {

    selectedYear = $('#year-selector option:selected').val();
    send_request();
});
$('#department-selector').change(function () {

    selectedDep = $('#department-selector option:selected').val();
    send_request();
});

function send_request() {
    'use strict';
    var depId = 'department_id=' + selectedDep + '';
    var yId = '&year_id=' + selectedYear + '';
    var bUrl = request_url + '?';
    var aUrl = bUrl + depId + yId;

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
    var randomScalingFactor = function () {
        return Math.round(Math.random() * 255)
    };

    var label_data = [];
    var review_item_label = [];
    var review_item = {};

    for (var i = 0; i < data.length; i++) {
        if (!label_data.includes(data[i].year)) {
            label_data.push(data[i].year);
        }
        if (review_item_label.includes(data[i].review_item__name)) {
            review_item[data[i].review_item__name].push(data[i].rate__avg);
        } else {
            review_item_label.push(data[i].review_item__name);
            review_item[data[i].review_item__name] = [];
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
                            beginAtZero: true,
                            max: 3
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