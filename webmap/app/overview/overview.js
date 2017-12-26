'use strict';

angular.module('houseApp.overview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/overview', {
    templateUrl: 'app/overview/overview.html',
    controller: 'OverviewCtrl'
  });
}])

.controller('OverviewCtrl', ['$scope', function($scope) {
	$scope.test = "xxxxxx";
	$('.map').maphilight();

}]);