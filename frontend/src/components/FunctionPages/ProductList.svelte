<!--
Component: ProductList.svelte
Description: This component displays a list of products in a table format, allowing users to select products for further actions.
Properties:
  - filteredProducts (array): List of products to display, filtered based on search criteria.
  - selectedProducts (Set): Set of product IDs selected for actions like update or delete.
Internal Variables:
  - None
Main Functions:
  - toggleSelect(productId): Toggles the selection of a product based on its ID.
External Dependencies:
  - formatToCOP from '../../lib/utils.js': Function to format numbers to Colombian Peso (COP) currency format.
-->

<script>
  import { formatToCOP } from '../../lib/utils.js';

  export let filteredProducts = [];
  export let selectedProducts = new Set();

  /**
   * Toggles the selection of a product.
   * @param {number} productId - ID of the product to select or deselect.
   */
  function toggleSelect(productId) {
    if (selectedProducts.has(productId)) {
      selectedProducts.delete(productId);
    } else {
      selectedProducts.add(productId);
    }
    selectedProducts = new Set(selectedProducts); 
  }
</script>

<table>
  <colgroup>
    <col style="width:10%">
    <col style="width:30%"> 
    <col style="width:15%"> 
    <col style="width:15%"> 
    <col style="width:30%"> 
  </colgroup>
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
        <td>{product.quantity}</td>
        <td>{formatToCOP(product.price)}</td>
        <td>{formatToCOP(product.quantity * product.price)}</td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  
  * {
    box-sizing: border-box;
  }

  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    margin: 0; 
  }

  td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ddd;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  
  tbody tr:first-child td {
    border-top: none;
  }

  
  tr:hover {
    background-color: #f1f1f1;
  }
</style>
