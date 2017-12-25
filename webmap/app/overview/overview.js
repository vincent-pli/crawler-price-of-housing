'use strict';

angular.module('houseApp.overview', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/overview', {
    templateUrl: 'overview/overview.html',
    controller: 'OverviewCtrl'
  });
}])

.controller('OverviewCtrl', [function() {
	console.log("That's overview...");

}]);