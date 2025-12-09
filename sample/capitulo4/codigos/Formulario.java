public class Formulario {

    private String id;
    private String descricao; // Conteudo principal
    private String objetivo; // Conteudo principal
    private List<Pergunta> perguntas; // Composição   
    private TipoStatus status;
    private int versao;
    private String idOriginal;
    private List<Historico> historico; // Composição
    private String criadoPor; // Metadados
    private LocalDateTime criadoEm; // Metadados
    private String modificadoPor; // Metadados
    private LocalDateTime modificadoEm; // Metadados
}