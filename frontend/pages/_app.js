/**
 * Custom App component for Next.js.
 * This component is used to initialize pages.
 *
 * @param {Object} props - The properties object.
 * @param {React.ComponentType} props.Component - The active page component.
 * @param {Object} props.pageProps - The initial props for the active page component.
 * @returns {JSX.Element} The active page component with its props.
 */
// frontend/pages/_app.js

import "../styles/globals.css";

/**
 * MyApp is the custom App component for the Next.js application.
 * It is used to initialize pages and can be used to keep state when navigating between pages.
 *
 * @param {Object} props - The properties passed to the component.
 * @param {React.ComponentType} props.Component - The active page component.
 * @param {Object} props.pageProps - The initial props that were preloaded for the page.
 * @returns {JSX.Element} The component to be rendered.
 */
function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />;
}

export default MyApp;
