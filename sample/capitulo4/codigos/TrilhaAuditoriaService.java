package com.rodrigo.trackForms.service;

import ...

@RequiredArgsConstructor
@Service
public class TrilhaAuditoriaService {

    private final TrilhaAuditoriaRepository trilhaAuditoriaRepository;

        public boolean registrar(Object antesObj, Object depoisObj, String tipoObjeto, String acao, String comentarios, String usuario, LocalDateTime dataHoraEvento) {
        try {
            TrilhaAuditoria trilha = TrilhaAuditoriaFactory.gerarRegistroTrilha(antesObj, depoisObj, tipoObjeto, acao, comentarios, usuario, dataHoraEvento);
            trilhaAuditoriaRepository.save(trilha);
            return true;
        } catch (Exception e) {
            return false;
        }
    }
    
    public Map<String, Object> listarTrilhas() {
        List<TrilhaAuditoria> trilhas = trilhaAuditoriaRepository.findAll();
        String mensagem = trilhas.isEmpty() ? "Trilha de auditoria não encontrada." : "Busca realizada com sucesso!";
        return Map.of("mensagem", mensagem, "trilhas", trilhas);
    }
}