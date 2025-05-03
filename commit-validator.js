#!/usr/bin/env node

const { execSync } = require("child_process");

// Ejecutar commitlint con --verbose
try {
  // Detectar si estamos en Windows o Unix
  const isWindows = process.platform === "win32";
  const paramVar = isWindows ? "%1" : "$1";

  execSync(`npx --no -- commitlint --edit ${paramVar} --verbose`, {
    stdio: "inherit",
    shell: true,
  });
} catch (error) {
  console.log("\n\n🔍 Formato correcto de commits:\n");
  console.log("  <tipo>(<ámbito opcional>): <descripción>");
  console.log("\nTipos permitidos:");
  console.log("  feat     ✨ Nueva característica");
  console.log("  fix      🐛 Corrección de error");
  console.log("  docs     📚 Documentación");
  console.log("  style    💎 Cambios de formato/estilo");
  console.log("  refactor 🔨 Refactorización de código");
  console.log("  perf     ⚡️ Mejoras de rendimiento");
  console.log("  test     🧪 Pruebas");
  console.log("  build    📦 Cambios en el sistema de build");
  console.log("  ci       🔄 Cambios en la integración continua");
  console.log("  chore    🧹 Tareas rutinarias");
  console.log("  revert   ⏪ Revierte un commit anterior");
  console.log("\nEjemplos:");
  console.log("  feat: añadir botón de login");
  console.log("  fix(auth): corregir problema al iniciar sesión");
  console.log("  docs: actualizar README con nuevas instrucciones");
  console.log(
    "\nMás información: https://www.conventionalcommits.org/es/v1.0.0/\n"
  );
  // El resto del script permanece igual...
  console.log("\n\n🔍 Formato correcto de commits:\n");
  // ...
  process.exit(1);
}
