<!--
Component: AddProductPopup.svelte
Description: This component displays a popup form to create a new product.
It allows capturing the product's name, price, and quantity, ensuring that it does not already exist in the database.
Properties: 
  - isOpen (boolean): Defines whether the popup is open or closed.
  - onSubmit (function): Callback executed upon form submission, receives the product object as an argument.
Internal Variables:
  - productName (string): Stores the entered product name.
  - productPrice (string): Stores the entered product price.
  - productQuantity (string): Stores the entered product quantity.
  - errorMessage (string): Contains an error message in case of validation failure.
Main Functions:
  - handleSubmit(): Validates and submits the form.
  - checkIfProductExists(name): Checks if a product with the entered name already exists.
  - resetForm(): Resets the form values.
  - openPopup(): Opens the popup.
  - closePopup(): Closes the popup.
External Dependencies:
  - Requires a backend at `http://localhost:5000` to handle creation and verification requests.
-->

<script>
  export let isOpen = false; // Defines whether the popup is visible or not
  export let onSubmit = (product) => {}; // Callback to handle form submission
  
  // Internal variables to store form values
  let productName = '';
  let productPrice = '';
  let productQuantity = '';
  let errorMessage = ''; // Stores error messages

  // Submits the form after validating the data
  async function handleSubmit() {
    if (!productName || isNaN(productPrice) || isNaN(productQuantity) || productPrice < 0 || productQuantity < 0) {
      console.error('Los valores del producto no son válidos');
      return;
    }

    // Checks if the product already exists
    const productExists = await checkIfProductExists(productName);
    if (productExists) {
      errorMessage = 'Ya existe un producto con ese nombre';
      return;
    }

    // Creates the product object
    const product = {
      name: productName,
      precio: parseFloat(productPrice),
      cantidad: parseInt(productQuantity),
    };

    // Attempts to send data to the server
    try {
      const response = await fetch('http://localhost:5000/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(product),
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error('Error al crear el producto:', errorText);
        throw new Error('Error al crear el producto');
      }

      onSubmit(product); // Calls the submission callback
      resetForm(); // Resets the form values
      closePopup(); // Closes the popup
    } catch (error) {
      console.error('Error en el submit:', error);
    }
  }

  // Checks if a product with the same name already exists in the database
  async function checkIfProductExists(name) {
    try {
      const response = await fetch('http://localhost:5000/products');
      const products = await response.json();

      return products.some(product => product.name.toLowerCase() === name.toLowerCase());
    } catch (error) {
      console.error('Error al verificar el producto:', error);
      return false;
    }
  }

  // Resets the form values
  function resetForm() {
    productName = '';
    productPrice = '';
    productQuantity = '';
    errorMessage = '';
  }

  // Opens the popup
  function openPopup() {
    isOpen = true;
  }

  // Closes the popup
  function closePopup() {
    isOpen = false;
  }
</script>

<!-- Button to open the popup -->
<button class="add-button" type="button" on:click={openPopup}>
  <span class="button__text">Añadir</span>
  <span class="button__icon">
    <svg 
      class="svg" 
      fill="none" 
      height="24" 
      stroke="currentColor" 
      stroke-linecap="round" 
      stroke-linejoin="round" 
      stroke-width="2" 
      viewBox="0 0 24 24" 
      width="24" 
      xmlns="http://www.w3.org/2000/svg">
      <line x1="12" x2="12" y1="5" y2="19"></line>
      <line x1="5" x2="19" y1="12" y2="12"></line>
    </svg>
  </span>
</button>

<!-- Popup containing the form -->
{#if isOpen}
  <div class="popup-overlay">
    <div class="popup-content">
      <h3>Crear Producto</h3>
      <form on:submit|preventDefault={handleSubmit}>
        <!-- Field to enter the product name -->
        <div class="form-group">
          <label for="name">Nombre</label>
          <input type="text" id="name" bind:value={productName} required />
        </div>
        <!-- Field to enter the price -->
        <div class="form-group">
          <label for="price">Precio</label>
          <input type="number" id="price" bind:value={productPrice} min="0" required />
        </div>
        <!-- Field to enter the quantity -->
        <div class="form-group">
          <label for="quantity">Cantidad</label>
          <input type="number" id="quantity" bind:value={productQuantity} min="0" required />
        </div>
        <!-- Error message if validation fails -->
        {#if errorMessage}
          <div class="error-message">{errorMessage}</div>
        {/if}
        <!-- Action buttons -->
        <div class="popup-actions">
          <button class="cancel-button" type="button" on:click={closePopup}>Cancelar</button>
          <button class="create-button" type="submit">Crear</button>
        </div>
      </form>
    </div>
  </div>
{/if}

<style>
  /* Styles for the "Add" Button */
  .add-button {
    display: flex;
    align-items: center;
    background-color: #eee;
    border: 2px solid #323232;
    box-shadow: 4px 4px #323232;
    border-radius: 10px;
    padding: 0;
    width: 150px;
    height: 40px;
    cursor: pointer;
    overflow: hidden;
    position: relative;
  }

  .add-button .button__text {
    margin-left: 30px;
    color: #323232;
    font-weight: 600;
    transition: all 0.3s;
  }

  .add-button .button__icon {
    position: absolute;
    right: 0;
    width: 39px;
    height: 100%;
    background-color: #dedede;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
  }

  .add-button:hover .button__text {
    color: transparent;
  }

  .add-button:hover .button__icon {
    width: 100%;
  }

  .add-button:active {
    transform: translate(3px, 3px);
    box-shadow: none;
  }

  .add-button:focus {
    outline: none;
  }

  /* Styles for the Overlay and Content */
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .popup-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    width: 300px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  }

  .popup-content h3 {
    text-align: center;
    margin-bottom: 15px;
    color: #323232;
  }

  .form-group {
    margin-bottom: 15px;
    display: flex;
    flex-direction: column;
  }

  .form-group label {
    margin-bottom: 5px;
    font-weight: 600;
    color: #323232;
  }

  .form-group input {
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  .error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
  }

  .popup-actions {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
    gap: 10px;
  }

  .popup-actions button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    color: #fff;
  }

  .cancel-button {
    background-color: #f44336; /* Red */
  }

  .create-button {
    background-color: #4caf50; /* Green */
  }
</style>