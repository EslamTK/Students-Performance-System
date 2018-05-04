window.onload = default_;
$('#year-selector').change(function () {	
	// erase old data from chart when update data 
		if(window.chart !== undefined || window.chart !== null){
			window.chart.destroy();
			}
        selectedYear=$( '#year-selector option:selected' ).val();
		//condition to disabe department_list till select year
	    if(selectedYear === ''){
			$("#department-selector").val($("#department-selector option:first").val());
            $('#department-selector').attr('disabled', 'disabled');
			default_();
		}else{
			$('#department-selector').attr('disabled', false);
			//$('#yTitle').attr('disabled', 'disabled');
			$('#dTitle').attr('disabled', 'disabled');
		}	
		console.log("Id: "+selectedYear);
		$('#department-selector').change(function () {	
			var selectedDep=$( '#department-selector option:selected' ).val();
			// send selected year and dep to send_request function 
			send_request(selectedYear,selectedDep);
		});
    });
function send_request(selectedYear,selectedDep) {
    'use strict';
	console.log("selectedYear: "+selectedYear);
	console.log("selectedDep: "+selectedDep);
    var depId = 'department_id='+selectedDep+'';
    var yId = '&year='+selectedYear+'';
    var bUrl = 'http://127.0.0.1:8000/dashboard/administrator_educators_rating?';
    var aUrl = bUrl + depId + yId ;

    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        data: JSON.stringify( { } ),
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
            window.chart = new Chart(ctx, {
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
}

function default_() {
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