<!--
Component: Sidebar.svelte
Description: This component renders a sidebar with navigation buttons for the dashboard, inventory, and about pages.
Properties:
  - None
Internal Variables:
  - dispatch (function): Dispatcher to emit custom navigation events.
Main Functions:
  - navigateTo(page): Dispatches a navigation event to the specified page.
  - handleKeyPress(event, page): Handles keyboard navigation using Enter or Space keys.
External Dependencies:
  - createEventDispatcher from Svelte: Used for event communication between components.
-->
<script>
  // Import createEventDispatcher from Svelte to handle communication between components
  import { createEventDispatcher } from 'svelte';
  
  // Create an event dispatcher
  const dispatch = createEventDispatcher();

  /**
   * Navigates to the specified page by dispatching a 'navigate' event.
   * @param {string} page - The page to navigate to.
   */
  function navigateTo(page) {
    dispatch('navigate', page);
  }

  /**
   * Handles navigation using Enter or Space keys.
   * @param {Event} event - The keyboard event.
   * @param {string} page - The page to navigate to.
   */
  function handleKeyPress(event, page) {
    if (event.key === 'Enter' || event.key === ' ') {
      navigateTo(page);
    }
  }
</script>

<!-- Main container for the sidebar -->
<div class="sidebar">
  <article class="sidebar-container">
    
    <!-- Button to navigate to Dashboard -->
    <button class="Btn" on:click={() => navigateTo('dashboard')} on:keydown={(event) => handleKeyPress(event, 'dashboard')} tabindex="0">
      <div class="sign">
        <img src="/assets/img/dashboard.svg" alt="Dashboard Icon" class="icon-img"/>
      </div>
      <div class="text">Dashboard</div>
    </button>

    <!-- Button to navigate to Inventory -->
    <button class="Btn" on:click={() => navigateTo('products')} on:keydown={(event) => handleKeyPress(event, 'products')} tabindex="0">
      <div class="sign">
        <img src="/assets/img/inventory.svg" alt="Products Icon" class="icon-img"/>
      </div>
      <div class="text">Inventario</div>
    </button>

    <!-- Button to navigate to About -->
    <button class="Btn" on:click={() => navigateTo('about')} on:keydown={(event) => handleKeyPress(event, 'about')} tabindex="0">
      <div class="sign">
        <img src="/assets/img/about.svg" alt="About Icon" class="icon-img"/>
      </div>
      <div class="text">Acerca de..</div>
    </button>

  </article>
</div>

<style>
  /* 
    Sidebar container.
    Sets width, height, background color, padding, shadow, and z-index.
  */
  .sidebar {
    width: 45px;
    height: 100vh;
    background-color: #1A1A1A;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    overflow: visible;
    z-index: 1000;
  }

  /* 
    Container for the sidebar buttons.
    Arranges buttons in a column with spacing.
  */
  .sidebar-container {
    display: flex;
    flex-direction: column;
    gap: 25px;
  }

  /* 
    Styles for the navigation buttons.
    Sets display, alignment, size, border, cursor, shadow, background color, and transition.
  */
  .Btn {
    --black: #000000;
    --ch-black: #141414;
    --eer-black: #1b1b1b;
    --night-rider: #2e2e2e;
    --white: #ffffff;
    --af-white: #f3f3f3;
    --ch-white: #e1e1e1;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 100%;
    height: 45px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition-duration: .3s;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.199);
    background-color: var(--night-rider);
  }

  /* 
    Container for the icon within the button.
    Sets size, alignment, and transition.
  */
  .sign {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition-duration: .3s;
  }

  /* 
    Styles for the icon images.
    Sets size.
  */
   .sign img  {
    width: 20px;
    height: 20px;
  }

 /* 
    Ensures the icon image uses the specified fill color.
  */
 .sign img  {
    fill: var(--af-white);
  }

  /* 
    Styles for the button text.
    Sets margin, opacity, color, font size, weight, transition, and text overflow handling.
  */
  .text {
    margin-left: 10px;
    opacity: 0;
    color: var(--af-white);
    font-size: 1.2em;
    font-weight: 600;
    transition-duration: .3s;
    white-space: nowrap; /* Prevents text from breaking into multiple lines */
    overflow: hidden; /* Ensures text does not overflow */
    max-width: 100%;
  }

  /* 
    Shows the button text on hover by changing opacity.
  */
  .Btn:hover .text {
    opacity: 1;
  }

  /* 
    Expands the button width on hover and maintains border radius.
  */
  .Btn:hover {
    width: 180px; /* Increases the container size only on mouse hover */
    border-radius: 5px;
  }
</style>