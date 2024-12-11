<!--
Component: App.svelte
Description: This is the main application component that manages navigation between different pages such as Welcome, Dashboard, Inventory, and About Us.
Properties:
  - None
Internal Variables:
  - currentPage (string): Defines the currently displayed page. The default initial page is 'welcome'.
Main Functions:
  - None
External Dependencies:
  - Sidebar.svelte: Sidebar component for navigation.
  - WelcomePage.svelte: Welcome page component.
  - Dashboard.svelte: Dashboard page component.
  - InventoryPage.svelte: Inventory management page component.
  - AboutUs.svelte: About Us page component.
-->
<script>
  // Import the components and pages used in the application.
  import Sidebar from './components/Buttons/Sidebar.svelte';
  import WelcomePage from './pages/WelcomePage.svelte';
  import Dashboard from './pages/Dashboard.svelte';
  import InventoryPage from './pages/InventoryPage.svelte';
  import AboutUs from './components/FunctionPages/AboutUs.svelte';

  // Variable that defines the currently displayed page to the user.
  // The default initial page is 'welcome'.
  let currentPage = 'welcome';
</script>

<!-- Main container of the application -->
<div class="app-container">
  <!-- Displays the Sidebar if not on the welcome page -->
  {#if currentPage !== 'welcome'}
    <!-- Sidebar: Side menu for navigating between pages -->
    <Sidebar on:navigate={(e) => currentPage = e.detail} />
  {/if}

  <main>
    <!-- Welcome screen -->
    {#if currentPage === 'welcome'}
      <WelcomePage on:enter={() => currentPage = 'dashboard'} />
    <!-- Main dashboard page -->
    {:else if currentPage === 'dashboard'}
      <Dashboard />
    <!-- Inventory management page -->
    {:else if currentPage === 'products'}
      <InventoryPage />
    <!-- About Us information page -->
    {:else if currentPage === 'about'}
      <AboutUs />
    {/if}
  </main>
</div>

<style>
  /* 
    Main container that combines the Sidebar and the main content.
    Uses flexbox for layout and occupies the full viewport height.
  */
  .app-container {
    display: flex;
    height: 100vh;
  }

  /* 
    Main content styling.
    Allows the main content to grow and occupy remaining space,
    adds padding, sets a light background color, and enables vertical scrolling if needed.
  */
  main {
    flex-grow: 1; /* The main content occupies the remaining space */
    padding: 20px; /* Internal spacing */
    background-color: #f5f5f5; /* Light background */
    overflow-y: auto; /* Enables vertical scrolling if necessary */
  }
</style>