window.onload = default_;
var selectedYear;
var flag=0;//flag to save the state of the term button =>(first or second) in window.term_id before select the year and dep
window.selected_year = null;
window.selected_dep = null;
$('#year-selector').change(function () {	
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
    var depId = 'department_id='+selectedDep+'';
    var yId = '&year_id='+selectedYear+'';
	if(t_id===null)
		{
			var tId = '&term_id='+term_id+'';
		}else{
			var tId = '&term_id='+t_id+'';
		}
    console.log("term_iddd: "+tId);
    //var tId = '&term_id='+term_id+'';
    var bUrl = 'http://127.0.0.1:8000/dashboard/educator_courses_counts?';
    var aUrl ;
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
        data: JSON.stringify( { } ),
        success: function (data) {
            console.log(data.result);
            // transform json array into normal array
            var course_name = data.result.map(function(result) {
            return result.course__name;
           });
            var mt_pass = data.result.map(function(result) {
            return result.midterm_pass;
           });
            var fin_pass = data.result.map(function(result) {
            return result.final_pass;
           });
            var ttl = data.result.map(function(result) {
            return result.total;
           });
            // subtract total - pass 
            var mt_fail = ttl.map(function (ttl, idx) {
              return ttl - mt_pass[idx];
            });
           var fin_fail = ttl.map(function (ttl, idx) {
              return ttl - fin_pass[idx];
            });

/////////////
            var barChartData = {
            labels: course_name,
            datasets: [
                {
                    label: 'Midterm Pass',
                    backgroundColor: 'rgba(220,220,220,0.2)',
                    borderColor: 'rgba(220,220,220,1)',
                    pointBackgroundColor: 'rgba(220,220,220,1)',
                    pointBorderColor: '#fff',
                    data: mt_pass
                },
                {
                    label: 'Midterm Fail',
                    backgroundColor: 'rgba(151,187,205,0.2)',
                    borderColor: 'rgba(151,187,205,1)',
                    pointBackgroundColor: 'rgba(151,187,205,1)',
                    pointBorderColor: '#fff',
                    pointBorderColor: '#fff',

                    data: mt_fail
                }
                ,
                {
                    label: 'Final Pass',
                    backgroundColor: 'rgba(234,209,204,0.2)',
                    borderColor: 'rgba(234,209,204,1)',
                    pointBackgroundColor: 'rgba(234,209,204,1)',

                    pointBorderColor: '#fff',
                    data: fin_pass
                }
                ,
                {
                    label: 'Final Fail',
                    backgroundColor: 'rgba(41,54,61,0.2)',
                    borderColor: 'rgba(41,54,61,1)',
                    pointBackgroundColor: 'rgba(41,54,61,1)',

                    pointBorderColor: '#fff',
                    data: fin_fail
                }
            ]
        }


        var ctx = document.getElementById('canvas-1');
        var chart = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: {
                responsive: true
            }
        });

////////////
        }
        });
    }




function default_() {
    'use strict';

    var randomScalingFactor = function () {
        return Math.round(Math.random() * 10)
    };

    var my_data = document.getElementById("myVar").value;

    //formating data to valid json format
    var data = my_data.slice(10, my_data.length, my_data)
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

        if (data[i].midterm_pass == 0) {
           
            label_data.push(data[i].course__name);
            midPass.push(data[i].midterm_pass);
            midFail.push(data[i].total - data[i].midterm_pass);
            finalPass.push(data[i].final_pass);
            finalFail.push(data[i].total - data[i].final_pass);
        }
    }


    var lineChartData = {
        labels: label_data,
        datasets: [
            {
                label: 'Midterm Pass',
                backgroundColor: 'rgba(220,220,220,0.2)',
                borderColor: 'rgba(220,220,220,1)',
                pointBackgroundColor: 'rgba(220,220,220,1)',
                pointBorderColor: '#fff',
                data: midPass
            },
            {
                label: 'Midterm Fail',
                backgroundColor: 'rgba(151,187,205,0.2)',
                borderColor: 'rgba(151,187,205,1)',
                pointBackgroundColor: 'rgba(151,187,205,1)',
                pointBorderColor: '#fff',
                pointBorderColor: '#fff',

                data: midFail
            }
            ,
            {
                label: 'Final Pass',
                backgroundColor: 'rgba(234,209,204,0.2)',
                borderColor: 'rgba(234,209,204,1)',
                pointBackgroundColor: 'rgba(234,209,204,1)',

                pointBorderColor: '#fff',
                data: finalPass
            }
            ,
            {
                label: 'Final Fail',
                backgroundColor: 'rgba(41,54,61,0.2)',
                borderColor: 'rgba(41,54,61,1)',
                pointBackgroundColor: 'rgba(41,54,61,1)',

                pointBorderColor: '#fff',
                data: finalFail
            }
        ]
    }


    var ctx = document.getElementById('canvas-1');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: lineChartData,
        options: {
            responsive: true
        }
    });
}
