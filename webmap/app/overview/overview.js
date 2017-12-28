'use strict';

angular.module('houseApp.overview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/overview', {
    templateUrl: 'app/overview/overview.html',
    controller: 'OverviewCtrl'
  });
}])

.controller('OverviewCtrl', ['$scope', function($scope) {
	$('.information').css({
    	position: 'absolute'
	}).hide();

	$('area').each(function(i) {
	    $('area').eq(i).bind('mouseover', function(e) {
	        $('.information').eq(i).css({
	            top: e.pageY,
	            left: e.pageX
	        }).show();
	    });
	    $('area').eq(i).bind('mouseout', function() {
	        $('.information').hide();
	    });
	});

	$('.map').maphilight();


	$scope.areaClick = function(element){

	};

	$scope.test = function(){
		console.log("hahahahah");
	};

}]);