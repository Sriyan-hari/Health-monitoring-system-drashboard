<?php
header("Content-Type: application/json");

$dataFile = "sensor_data.txt";
if (file_exists($dataFile)) {
    $data = file_get_contents($dataFile);
    $sensorData = explode(",", $data);
    $response = [
        "temperature" => intval($sensorData[1]),
        "pulse" => intval($sensorData[0])
    ];
    echo json_encode($response);
} else {
    echo json_encode(["error" => "No data available"]);
}
