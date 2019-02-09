$(function () {
    eventListeners();
});

const eventListeners = function () {
    $('.js-btn-theatre').on('click', function () {
        getUserCurrentLocation();
    });
};

const redirectTheatreList = function (position) {
    window.location.href = `/fun/theatres/${position.coords.longitude}/${position.coords.latitude}/`;
};

const blockLocation = function (error) {
    $.sweetModal({
        content: 'Your current location is unavailable.',
        title: 'Obtain Location',
        icon: $.sweetModal.ICON_WARNING,
});
    return 0;
}
const getUserCurrentLocation = function () {
  navigator.geolocation.getCurrentPosition(function (position) {
      redirectTheatreList(position)
  }, function (error) {blockLocation(error)})
};