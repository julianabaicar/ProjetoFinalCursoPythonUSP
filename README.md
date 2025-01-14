# Tarefa de programação: Programa completo - Similaridades entre textos - Caso COH-PIAH

## Prólogo
    Neste último exercício da Parte 1, iremos praticar não só o que vimos até agora no curso mas também outra habilidade importante de um programador: utilizar e interagir com código escrito por terceiros. Aqui, você não irá implementar o seu programa do zero. Você irá partir de um programa já iniciado e irá completá-lo. Na verdade, esse é o caso mais comum na indústria de software, onde muitos desenvolvedores trabalham colaborativamente em um mesmo programa.

## Introdução 
    Manuel Estandarte é monitor na disciplina Introdução à Produção Textual I na Universidade de Pasárgada (UPA). Durante o período letivo, Manuel descobriu que uma epidemia de COH-PIAH estava se espalhando pela UPA. Essa doença rara e altamente contagiosa faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Após a entrega da primeira redação, Manuel desconfiou que alguns alunos estavam sofrendo de COH-PIAH. Manuel, preocupado com a saúde da turma, resolveu buscar um método para identificar os casos de COH-PIAH. Para isso, ele necessita da sua ajuda para desenvolver um programa que o auxilie a identificar os alunos contaminados.

## Detecção de autoria
    Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.

    ### Traços linguísticos
        Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

            Tamanho médio de palavra: Média simples do número de caracteres por palavra.

            Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

            Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.

            Tamanho médio de sentença: Média simples do número de caracteres por sentença.

            Complexidade de sentença: Média simples do número de frases por sentença.

            Tamanho médio de frase: Média simples do número de caracteres por frase.


## Concluindo
   
    Basicamente, sua tarefa é implementar corretamente as seguintes funções:  

        compara_assinatura(as_a, as_b)

        calcula_assinatura(texto)

        avalia_textos(textos, ass_cp)

        Usando o esqueleto que oferecemos acima e implementando essas 3 funções, seu detector de plágio estará completo e você poderá submetê-lo ao corretor automático. Caso o corretor automático aponte erros, tente ler com bastante cuidado e atenção a mensagem fornecida por ele, pois ela normalmente ajuda a identificar o erro.   

