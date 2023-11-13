<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "Hotel";
$port = "3306";

// Crear conexión
$conn = new mysqli($servername, $username, $password, $dbname, $port);

// Verificar conexión
if ($conn->connect_error) {
  die("Conexión fallida: " . $conn->connect_error);
}

// Revisa si el formulario fue enviado
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_input = $_POST['username'];

    // La consulta vulnerable a inyección SQL
    $sql = "SELECT * FROM usuarios WHERE nombre_usuario = '$user_input'";
    
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Mostrar los resultados si los hay
        while($row = $result->fetch_assoc()) {
            echo "id: " . $row["id"]. " - Nombre: " . $row["nombre_usuario"]. " " . $row["contraseña"]. "<br>";
        }
    } else {
        echo "0 resultados";
    }
} else {
    echo "Por favor ingrese un nombre de usuario.";
}

$conn->close();
?>
