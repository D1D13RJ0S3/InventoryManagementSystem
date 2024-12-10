<!--
Component: ProductList.svelte
Description: This component displays a list of products in a table format.
It allows users to select products using checkboxes and displays product details such as name, quantity, and price.
Properties:
  - filteredProducts (array): The list of filtered products to display.
  - selectedProducts (Set): A set of selected product IDs.
Internal Variables:
  - None
Main Functions:
  - toggleSelect(productId): Toggles the selection of a product by its ID.
External Dependencies:
  - formatToCOP: A utility function to format prices to Colombian Pesos.
-->
<script>
  import { formatToCOP } from '../../lib/utils.js';

  // Receives the filtered products from the parent component
  export let filteredProducts = [];
  export let selectedProducts = new Set();

  // Function to toggle the selection of products
  function toggleSelect(productId) {
    if (selectedProducts.has(productId)) {
      selectedProducts.delete(productId);
    } else {
      selectedProducts.add(productId);
    }
    selectedProducts = new Set(selectedProducts); // Force reactivity
  }
</script>

<table>
  <thead>
    <tr>
      <th>Seleccionar</th>
      <th>Nombre</th>
      <th>Cantidad</th>
      <th>Precio</th>
    </tr>
  </thead>
  <tbody>
    {#each filteredProducts as product}
      <tr>
        <td>
          <input
            type="checkbox"
            on:change={() => toggleSelect(product.id)}
            checked={selectedProducts.has(product.id)}
          />
        </td>
        <td>{product.name}</td>
        <td>{product.cantidad}</td>
        <td>{formatToCOP(product.precio)}</td>
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