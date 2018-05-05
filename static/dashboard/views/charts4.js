window.onload = default_;
var selectedYear;
var flag=0;//flag to save the state of the term button =>(first or second) in window.term_id before select the year and dep
window.selected_year = null;
window.selected_dep = null;
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
			//$('#activated').attr('class', 'focus active');
		}	
		console.log("Id: "+selectedYear);
		$('#department-selector').change(function () {	
			var selectedDep=$( '#department-selector option:selected' ).val();
			// send selected year and dep to send_request function 
			
			//------------set year & department values in global variables 
			if(selectedYear!==null && selectedDep!==null)
				{
					window.selected_year = selectedYear;
					window.selected_dep = selectedDep;
				}			
			//-------------if flag=0 that mean button not checked > then return null in its value
			if(flag===0){
				send_request(selectedYear,selectedDep,null);
			}else{ //---------else flag=1 that mean button checked > then return its value
				send_request(selectedYear,selectedDep,window.term_id);
				flag=0;//-------- return flag = 0 after execute the function 
			}	
		});
    });

    //function applied on change term 
	$("input:radio[name=options]").change(function(){
		// erase old data from chart when update data 
		if(window.chart !== undefined || window.chart !== null){
			window.chart.destroy();
			}
		var ter_id= $('input:radio[name=options]:checked').val();
		//console.log("here is : "+ter_id );
		window.term_id=ter_id; //make ter_id global variable
			flag=1;
		//------------------check if year & department are selected
		if(window.selected_year===null || window.selected_dep===null) {
			// if year & department not selected send request with selected term only.
			send_request(null,null,ter_id);
			}else{ //if year & department are selected send request with selected year, department & term.
					console.log("you select year: "+window.selected_year);
					console.log("you select dep: "+window.selected_dep);
				//send request with values of selected year, department & term.
					send_request(window.selected_year,window.selected_dep,ter_id);
				   
			}
		//---------------------------------------------
	});


//default value of radio button
var term_id=$("#rb").prop("checked", true).val();
console.log("test_term: "+term_id);

function send_request(selectedYear,selectedDep,t_id) {
    'use strict';
	console.log("selectedYear: "+selectedYear);
	console.log("selectedDep: "+selectedDep);
    var depId = 'department_id='+selectedDep+'';
    var yId = '&year='+selectedYear+'';
	if(t_id===null)
		{
			var tId = '&term_id='+term_id+'';
		}else{
			var tId = '&term_id='+t_id+'';
		}
    console.log("term_iddd: "+tId);
    var bUrl = 'http://127.0.0.1:8000/dashboard/administrator_years_counts?';
	var aUrl;
	// if year & department are not selected 
	//make url doesn't contain data& department values as url parameters
	if(selectedYear===null && selectedDep===null)
		{
		    aUrl = bUrl + tId;
		}else{
			aUrl = bUrl +  depId + yId + tId;
		}
     
    $.ajax({
        url: aUrl,
        dataType: "json",
        type: 'GET',
        contentType: 'application/json',
        success: function (data) {
            console.log(data);
            var label_data = [];
            var success = [];
            var fail = [];


            for (var i = 0; i < data.result.length; i++) {

                label_data.push(data.result[i].year);
                success.push(data.result[i].success);
                fail.push(data.result[i].fail);
                console.log(data.result[i].year);
                console.log(data.result[i].success);
                console.log(data.result[i].fail);
            }
            /////////
            var lineChartData = {
                labels: label_data,
                datasets: [
                    {
                        label: 'success',
                        backgroundColor: 'rgba(220,220,220,0.2)',
                        borderColor: 'rgba(220,220,220,1)',
                        pointBackgroundColor: 'rgba(220,220,220,1)',
                        pointBorderColor: '#fff',
                        data: success
                    },
                    {
                        label: 'Fail',
                        backgroundColor: 'rgba(151,187,205,0.2)',
                        borderColor: 'rgba(151,187,205,1)',
                        pointBackgroundColor: 'rgba(151,187,205,1)',
                        pointBorderColor: '#fff',
                        data: fail
                    }
                ]
            }


            var ctx = document.getElementById('canvas-1');
            window.chart = new Chart(ctx, {
                type: 'bar',
                data: lineChartData,
                options: {
                    scales: {
                yAxes: [{
                    display: true,
                    ticks: {
                        beginAtZero: true,
                        stepSize: 0.2,
                        max: 2
                           }
                     }]
                    },
                    responsive: true
                }
            });
            ///////////
        }
    });
}
  
function default_() {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 100)
    };

    //getting data from hidden input field
    var my_data = document.getElementById("myData").value;
    console.log(my_data);
    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
    data = data.replace('>', '');
    data = data.replace(/'/g, '"');
    data = JSON.parse(data);
    console.log(data);

    var label_data = [];
    var success = [];
    var fail = [];


    for (var i = 0; i < data.length; i++) {

        label_data.push(data[i].year);
        success.push(data[i].success);
        fail.push(data[i].fail);
    }

    var lineChartData = {
        labels: label_data,
        datasets: [
            {
                label: 'success',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: success
            },
            {
                label: 'Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                data: fail
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    window.chart = new Chart(ctx, {
        type: 'line',
        data: lineChartData,
        options: {
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                        max: 10
                    }
                }]
            }
        }
    });


}