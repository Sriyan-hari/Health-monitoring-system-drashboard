<?php
header("Content-Type: application/json");

$input = json_decode(file_get_contents("php://input"), true);
$command = $input["action"] == "ON" ? "BUZZER_ON" : "BUZZER_OFF";

// Use the correct IP address and port for your ESP device
$espSocket = fsockopen("192.168.1.10", 8081);  // Replace with the correct IP and port for the ESP device

if ($espSocket) {
    fwrite($espSocket, $command);
    fclose($espSocket);
    echo json_encode(["message" => "Command sent successfully"]);
} else {
    echo json_encode(["error" => "Failed to connect to device"]);
}
