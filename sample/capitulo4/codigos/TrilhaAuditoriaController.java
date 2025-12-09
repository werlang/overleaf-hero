package com.rodrigo.trackForms.controller;

import ...

@RestController
@RequestMapping("api/v1/audit")
@RequiredArgsConstructor
public class TrilhaAuditoriaController {

    private final TrilhaAuditoriaService trilhaAuditoriaService;

    @GetMapping
    public ResponseEntity<?> listar() {
        return ResponseEntity.ok(trilhaAuditoriaService.listarTrilhas());
    }
}
