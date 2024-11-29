<script>
  import ProductList from '../components/ProductList.svelte';
  import Button from '../components/Button.svelte';
  import Navbar from '../components/Navbar.svelte';
  import DeleteButton from '../components/DeleteButton.svelte';

  let searchTerm = ''; 

  
  function handleCreate() {
    console.log('Crear producto');
  }

  function handleUpdate() {
    console.log('Actualizar producto');
  }

  function handleDelete() {
    console.log('Eliminar producto');
  }
</script>

<div class="dashboard-container">
  <!-- Uso de un template de POWER BI para pruebas-->
  <section class="graph">
    <iframe
      title="Sample Report Demo"
      width="100%"
      height="400"
      src="https://playground.powerbi.com/sampleReportEmbed"
      frameborder="0"
      allowfullscreen="true">
    </iframe>
  </section>

  <!-- Barra de busqueda debajo del Power BI -->
  <div class="search-bar">
    <input
      type="text"
      placeholder="Buscar productos..."
      bind:value="{searchTerm}"
      class="search-input"
    />
  </div>

  <section class="inventory">
    <h2 class="inventory-title">Productos</h2>
    <ProductList {searchTerm} />
    <div class="actions">

      <div class="buttons-container">
        <Button label="Crear Producto" on:click={handleCreate} />
        <Button label="Actualizar Producto" on:click={handleUpdate} />
        <Button label="Eliminar Producto" on:click={handleDelete} />
      </div>
    </div>
  </section>
</div>

<style>
  .dashboard-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  
  .graph {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  
  .search-bar {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    display: flex;
    justify-content: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .search-input {
    width: 100%;
    max-width: 400px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
  }

  .inventory {
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  
  .inventory-title {
    text-align: center;
    margin-bottom: 20px;
  }

  
  .buttons-container {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
  }

  .actions {
    display: flex;
    gap: 10px;
    margin-top: 20px;
  }
</style>
