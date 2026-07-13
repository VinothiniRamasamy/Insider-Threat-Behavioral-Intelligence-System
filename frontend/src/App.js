import React, { useState } from "react";

import Login from "./Login";
import Guide from "./Guide";
import Dashboard from "./Dashboard";

function App() {

  const [user, setUser] = useState(null);
  const [page, setPage] = useState("login");

  const handleLogin = (loggedUser) => {
    setUser(loggedUser);
    setPage("guide");
  };

  const handleContinue = () => {
    setPage("dashboard");
  };

  const handleLogout = () => {
    setUser(null);
    setPage("login");
  };

  return (
    <>
      {page === "login" && (
        <Login onLogin={handleLogin} />
      )}

      {page === "guide" && (
        <Guide onContinue={handleContinue} />
      )}

      {page === "dashboard" && (
        <Dashboard
          user={user}
          onLogout={handleLogout}
        />
      )}
    </>
  );
}

export default App;