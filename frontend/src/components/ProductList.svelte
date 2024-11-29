<script>
  export let searchTerm = ''; 

  // Simular lista (NO SE IMPLEMENTARA AL FINAL)
  let productos = [
    { id: 1, nombre: 'Producto A', cantidad: 10, precio: 100 },
    { id: 2, nombre: 'Producto B', cantidad: 20, precio: 200 },
    { id: 3, nombre: 'Producto C', cantidad: 15, precio: 150 },
    { id: 4, nombre: 'Producto D', cantidad: 15, precio: 150 },
  ];

  // Filtrar productos por ID o Nombre
  $: productosFiltrados = productos.filter((producto) => {
    const lowercasedSearchTerm = searchTerm.toLowerCase();
    return (
      producto.nombre.toLowerCase().includes(lowercasedSearchTerm) || 
      producto.id.toString().includes(lowercasedSearchTerm)
    );
  });
</script>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Nombre</th>
      <th>Cantidad</th>
      <th>Precio</th>
    </tr>
  </thead>
  <tbody>
    {#each productosFiltrados as producto}
      <tr>
        <td>{producto.id}</td>
        <td>{producto.nombre}</td>
        <td>{producto.cantidad}</td>
        <td>{producto.precio}</td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th, td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd;
  }

  th {
    background-color: #f4f4f4;
  }
</style>
