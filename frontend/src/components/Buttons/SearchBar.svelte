<!--
Component: SearchBar.svelte
Description: This component provides a search input field for filtering products.
Properties:
  - searchTerm (string): The current search term entered by the user.
Internal Variables:
  - dispatch (function): Dispatcher to emit search events.
Main Functions:
  - handleInput(event): Handles user input, updates the search term, and dispatches the search event.
External Dependencies:
  - Uses Svelte's createEventDispatcher to handle event dispatching.
-->

<script>
  import { createEventDispatcher } from 'svelte';

  export let searchTerm = '';
  const dispatch = createEventDispatcher();

  // Handle the search term input
  function handleInput(event) {
    searchTerm = event.target.value;
    dispatch('search', { searchTerm });
  }
</script>

<input
  placeholder="Buscar Productos..."
  type="text"
  name="text"
  class="input"
  bind:value={searchTerm}
  on:input={handleInput}
/>

<style>
  .input {
    width: 100%;
    max-width: 220px;
    height: 45px;
    padding: 12px;
    border-radius: 12px;
    border: 1.5px solid lightgrey;
    outline: none;
    transition: all 0.3s cubic-bezier(0.19, 1, 0.22, 1);
    box-shadow: 0px 0px 20px -18px;
    box-sizing: border-box; /* Ensures padding is included in the total width */
  }

  .input:hover {
    border: 2px solid lightgrey;
    box-shadow: 0px 0px 20px -17px;
  }

  .input:active {
    transform: scale(0.95);
  }

  .input:focus {
    border: 2px solid grey;
  }

  /* Optional: Mobile device adaptation */
  @media (max-width: 600px) {
    .input {
      max-width: 100%;
      height: 40px;
      padding: 10px;
    }
  }
</style>