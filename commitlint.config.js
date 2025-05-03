module.exports = {
  extends: ["@commitlint/config-conventional"],
  helpUrl: "https://www.conventionalcommits.org/es/v1.0.0/",
  rules: {
    // Aquí puedes sobrescribir o añadir reglas
    "type-enum": [
      2,
      "always",
      [
        "build", // Cambios en el sistema de build o dependencias
        "chore", // Tareas rutinarias
        "ci", // Cambios en la integración continua
        "docs", // Documentación
        "feat", // Nuevas características
        "fix", // Corrección de errores
        "perf", // Mejoras de rendimiento
        "refactor", // Refactorizaciones
        "revert", // Revierte un commit anterior
        "style", // Cambios de estilo (formato)
        "test", // Pruebas
      ],
    ],
  },
};
