const socket = io('http://localhost:5000');

const videoFeed = document.getElementById('video-feed');
const loading = document.getElementById('loading');
const connectionStatus = document.getElementById('connection-status');
const southboundCount = document.getElementById('southbound-count');
const northboundCount = document.getElementById('northbound-count');
const totalCount = document.getElementById('total-count');
const fpsValue = document.getElementById('fps-value');
const northboundThumbnails = document.getElementById('northbound-thumbnails');
const southboundThumbnails = document.getElementById('southbound-thumbnails');

let stats = {
    southbound: 0,
    northbound: 0,
    total: 0,
    fps: 0
};

let northboundVehicles = [];
let southboundVehicles = [];
const MAX_THUMBNAILS = 10;

const vehicleTranslation = {
    'car': '汽車',
    'motorcycle': '機車'
};

socket.on('connect', () => {
    console.log('已連接到服務器');
    updateConnectionStatus('connected');
    loading.classList.add('hidden');
});

socket.on('disconnect', () => {
    console.log('與服務器斷開連接');
    updateConnectionStatus('disconnected');
    loading.classList.remove('hidden');
});

socket.on('video_frame', (data) => {
    videoFeed.src = 'data:image/jpeg;base64,' + data.frame;
});

socket.on('stats_update', (data) => {
    stats = data;
    updateStatsDisplay();
});

socket.on('new_vehicle', (data) => {
    addVehicleThumbnail(data);
});

function updateConnectionStatus(status) {
    connectionStatus.className = `status-badge ${status}`;
    const statusText = {
        'connected': '已連接',
        'connecting': '連接中',
        'disconnected': '已斷開'
    };
    connectionStatus.textContent = statusText[status] || '未知';
}

function updateStatsDisplay() {
    animateValue(southboundCount, parseInt(southboundCount.textContent), stats.southbound, 500);
    animateValue(northboundCount, parseInt(northboundCount.textContent), stats.northbound, 500);
    animateValue(totalCount, parseInt(totalCount.textContent), stats.total, 500);

    fpsValue.textContent = stats.fps.toFixed(1);
}

function animateValue(element, start, end, duration) {
    if (start === end) return;

    const range = end - start;
    const increment = range / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
        current += increment;
        if ((increment > 0 && current >= end) || (increment < 0 && current <= end)) {
            current = end;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current);
    }, 16);
}

function addVehicleThumbnail(vehicle) {
    const { direction, image, class: vehicleClass, timestamp } = vehicle;

    const thumbnailItem = document.createElement('div');
    thumbnailItem.className = 'thumbnail-item';

    const img = document.createElement('img');
    img.src = 'data:image/jpeg;base64,' + image;
    img.alt = vehicleClass;

    const info = document.createElement('div');
    info.className = 'thumbnail-info';

    const type = document.createElement('span');
    type.className = 'vehicle-type';
    type.textContent = vehicleTranslation[vehicleClass] || vehicleClass;

    const time = document.createElement('span');
    time.className = 'vehicle-time';
    time.textContent = timestamp;

    info.appendChild(type);
    info.appendChild(time);
    thumbnailItem.appendChild(img);
    thumbnailItem.appendChild(info);

    if (direction === 'northbound') {
        northboundVehicles.unshift(thumbnailItem);
        if (northboundVehicles.length > MAX_THUMBNAILS) {
            northboundVehicles.pop();
        }
        updateThumbnailList(northboundThumbnails, northboundVehicles);
    } else if (direction === 'southbound') {
        southboundVehicles.unshift(thumbnailItem);
        if (southboundVehicles.length > MAX_THUMBNAILS) {
            southboundVehicles.pop();
        }
        updateThumbnailList(southboundThumbnails, southboundVehicles);
    }
}

function updateThumbnailList(container, vehicles) {
    container.innerHTML = '';

    if (vehicles.length === 0) {
        const emptyMessage = document.createElement('div');
        emptyMessage.className = 'empty-message';
        emptyMessage.textContent = '暫無車輛記錄';
        container.appendChild(emptyMessage);
    } else {
        vehicles.forEach(vehicle => {
            container.appendChild(vehicle.cloneNode(true));
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    console.log('交通監控系統已啟動');
    updateConnectionStatus('connecting');
});

window.addEventListener('beforeunload', () => {
    socket.disconnect();
});
