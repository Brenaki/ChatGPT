import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;

public class BlocoDeNotas extends JFrame {

    private JTextArea textArea;
    private JFileChooser fileChooser;

    public BlocoDeNotas() {
        setTitle("Bloco de Notas");
        setSize(500, 500);
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // Cria uma barra de menu
        JMenuBar menuBar = new JMenuBar();

        // Cria o menu "Arquivo"
        JMenu arquivoMenu = new JMenu("Arquivo");
        JMenuItem novoMenuItem = new JMenuItem("Novo");
        JMenuItem abrirMenuItem = new JMenuItem("Abrir");
        JMenuItem salvarMenuItem = new JMenuItem("Salvar");
        JMenuItem sairMenuItem = new JMenuItem("Sair");

        // Adiciona os itens ao menu "Arquivo"
        arquivoMenu.add(novoMenuItem);
        arquivoMenu.add(abrirMenuItem);
        arquivoMenu.add(salvarMenuItem);
        arquivoMenu.addSeparator();
        arquivoMenu.add(sairMenuItem);

        // Adiciona o menu "Arquivo" à barra de menu
        menuBar.add(arquivoMenu);

        // Adiciona a barra de menu à janela
        setJMenuBar(menuBar);

        // Cria uma área de texto
        textArea = new JTextArea();

        // Cria uma barra de rolagem para a área de texto
        JScrollPane scrollPane = new JScrollPane(textArea);
        add(scrollPane);

        // Cria um seletor de arquivos
        fileChooser = new JFileChooser();

        // Adiciona um ouvinte de eventos para o menu "Novo"
        novoMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                textArea.setText("");
            }
        });

        // Adiciona um ouvinte de eventos para o menu "Abrir"
        abrirMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int escolha = fileChooser.showOpenDialog(BlocoDeNotas.this);
                if (escolha == JFileChooser.APPROVE_OPTION) {
                    File arquivo = fileChooser.getSelectedFile();
                    try {
                        FileReader reader = new FileReader(arquivo);
                        textArea.read(reader, null);
                        reader.close();
                    } catch (IOException ex) {
                        JOptionPane.showMessageDialog(BlocoDeNotas.this, "Erro ao abrir o arquivo.");
                    }
                }
            }
        });

        // Adiciona um ouvinte de eventos para o menu "Salvar"
        salvarMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                int escolha = fileChooser.showSaveDialog(BlocoDeNotas.this);
                if (escolha == JFileChooser.APPROVE_OPTION) {
                    File arquivo = fileChooser.getSelectedFile();
                    try {
                        FileWriter writer = new FileWriter(arquivo);
                        textArea.write(writer);
                        writer.close();
                    } catch (IOException ex) {
                        JOptionPane.showMessageDialog(BlocoDeNotas.this, "Erro ao salvar o arquivo.");
                    }
                }
            }
        });

        // Adiciona um ouvinte de eventos para o menu "Sair"
        sairMenuItem.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        BlocoDeNotas blocoDeNotas = new BlocoDeNotas();
        blocoDeNotas.setVisible(true);
    }
}
