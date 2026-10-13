"""Crea el índice /politicas/ y las 3 páginas de Políticas.

Contenido según los PDF de `rit-politicas/Politicas/*.txt` (RIT).
"""
from django.db import migrations

INDEX_BODY = [
    (
        "page_hero",
        {
            "badge": "Políticas",
            "title_pre": "Nuestras",
            "title_hi": "políticas",
            "lead": "Consulte las políticas corporativas que rigen nuestra operación.",
            "cta_label": "",
            "cta_href": "",
        },
    ),
    (
        "cta",
        {
            "title": "¿Necesita conocer nuestras políticas?",
            "body": "Los documentos que rigen nuestra operación están disponibles aquí.",
            "cta_label": "Contáctenos",
            "cta_href": "/contacto/",
        },
    ),
]


BODY_ETICA = (
    "<p>En RIT ENTERPRISE SOLUTIONS S.A.S. adoptamos este Código de Ética como el marco que "
    "orienta nuestro comportamiento y nuestras decisiones en todas las actividades que "
    "desarrollamos como empresa del sector de equipos de cómputo, servidores e "
    "infraestructura tecnológica. Creemos firmemente que la integridad, la transparencia, el "
    "respeto, la responsabilidad y el compromiso con la legalidad constituyen la base de "
    "nuestra cultura organizacional y del relacionamiento con nuestros colaboradores, "
    "clientes, proveedores, aliados estratégicos y la comunidad.</p><p>Para nosotros, actuar "
    "éticamente no es solo una obligación legal, sino una convicción que guía cada una de "
    "nuestras acciones.</p><p>A través de este Código definimos los principios, valores y "
    "estándares de conducta que todos debemos conocer, interiorizar y aplicar en el "
    "ejercicio de nuestras funciones.</p><p>Nos comprometemos a desarrollar nuestras "
    "operaciones bajo criterios de competencia leal, veracidad en la información, protección "
    "del consumidor y cumplimiento estricto de las normas comerciales, laborales, civiles, "
    "penales y administrativas vigentes en la República de Colombia, en especial las "
    "relacionadas con el Código Sustantivo del Trabajo, la Ley 1581 de 2012 sobre protección "
    "de datos personales, la Ley 1273 de 2009 sobre delitos informáticos, la Ley 1474 de "
    "2011 (Estatuto Anticorrupción), así como las disposiciones de la Superintendencia de "
    "Industria y Comercio y del Ministerio del Trabajo. Garantizamos el manejo seguro, ético "
    "y autorizado de la información técnica, financiera, estratégica y personal, el respeto "
    "por la propiedad intelectual, marcas, licencias de software y derechos de autor, la "
    "adecuada administración y custodia de los recursos físicos, tecnológicos y financieros "
    "de la empresa, la prevención y gestión transparente de los conflictos de interés y el "
    "rechazo absoluto de toda forma de corrupción.</p><p>Asimismo, rechazamos de manera "
    "categórica cualquier forma de soborno, fraude, conflicto de interés indebido, lavado de "
    "activos o financiación del terrorismo. Promovemos un ambiente laboral sano, seguro, "
    "incluyente y libre de acoso laboral, acoso sexual, discriminación o cualquier conducta "
    "que atente contra la dignidad humana. Consideramos que cada persona que hace parte de "
    "RIT ENTERPRISE SOLUTIONS S.A.S. tiene la responsabilidad de contribuir a una "
    "convivencia basada en el buen trato, la equidad y la justicia.</p><p>Nos comprometemos "
    "a cumplir la Constitución Política de Colombia, las leyes vigentes, el Reglamento "
    "Interno de Trabajo y todas las políticas corporativas que rigen nuestra actuación. "
    "Asumimos que el cumplimiento de este Código es condición esencial de nuestra relación "
    "laboral o contractual con la empresa; por ello, nos obligamos a reportar de buena fe "
    "cualquier situación que contraríe estos principios por los canales establecidos y "
    "aceptamos que su incumplimiento dará lugar a la aplicación de las medidas "
    "disciplinarias y legales correspondientes.</p><p>__________________________ JUAN ALVARO "
    "ROJAS ERASO Representante legal</p>"
)


BODY_SIG = (
    "<p>RIT ENTERPRISE SOLUTIONS S.A.S., empresa dedicada a proveer soluciones integrales en "
    "tecnologías de la información, incluyendo consultoría, diseño, implementación y soporte "
    "de infraestructura tecnológica, se compromete a:</p><p>Satisfacer los requisitos de sus "
    "clientes y partes interesadas, asegurando la calidad de sus productos y "
    "servicios.</p><p>Proteger la confidencialidad, integridad y disponibilidad de la "
    "información, garantizando su uso seguro y responsable.</p><p>Proporcionar condiciones "
    "de trabajo seguras y saludables, previniendo lesiones y enfermedades laborales, en "
    "cumplimiento del Decreto 1072 de 2015 y demás normativa aplicable.</p><p>Proteger el "
    "medio ambiente, previniendo la contaminación y gestionando adecuadamente los impactos "
    "ambientales derivados de sus actividades.</p><p>Promover el uso ético, seguro y "
    "responsable de las tecnologías e inteligencia artificial, conforme a buenas prácticas "
    "internacionales.</p><p>Cumplir con los requisitos legales, reglamentarios y otros "
    "compromisos suscritos por la organización.</p><p>Gestionar los riesgos y oportunidades "
    "asociados a sus procesos, asegurando la continuidad del negocio y la sostenibilidad "
    "organizacional.</p><p>Mejorar continuamente la eficacia, desempeño y madurez del "
    "Sistema Integrado de Gestión.</p><p>Para el cumplimiento de esta política, la "
    "organización se compromete a:</p><p>Identificar, evaluar y controlar los riesgos en "
    "seguridad y salud en el trabajo, así como los riesgos de seguridad de la información y "
    "operacionales.</p><p>Identificar los aspectos ambientales y gestionar sus impactos "
    "asociados.</p><p>Garantizar ambientes de trabajo seguros, mediante controles "
    "operacionales, tecnologías seguras y buenas prácticas.</p><p>Fortalecer las "
    "competencias del talento humano a través de programas de formación, capacitación y "
    "sensibilización.</p><p>Promover la consulta, participación y comunicación activa de los "
    "trabajadores y partes interesadas.</p><p>Proteger la información mediante controles de "
    "seguridad adecuados y gestión de accesos.</p><p>Implementar mecanismos de seguimiento, "
    "medición y mejora continua del desempeño del sistema.</p><p>Asignar los recursos "
    "humanos, técnicos y financieros necesarios para la implementación, mantenimiento y "
    "mejora del Sistema Integrado de Gestión.</p><p>Esta política será divulgada, "
    "comprendida y aplicada en todos los niveles de la organización y estará disponible para "
    "las partes interesadas, siendo revisada periódicamente para asegurar su pertinencia y "
    "alineación con la estrategia organizacional.</p><p>Se firma en la ciudad de Bogotá a "
    "los 30 días del mes de abril del 2026</p><p>_______________________________________ "
    "JUAN ALVARO ROJAS C.C: 12.991.662 de San Juan (Pasto) Representante Legal Gerente "
    "General</p>"
)


BODY_DATOS = (
    "<p>Razon social: RIT ENTERPRISE SOLUTIONS SAS</p><p>Nit: 900.836.520-1</p><p>Domicilio: "
    "Av Carrera 9 No. 115-06/30 Ed. Tierra Firme, Oficina 1207</p><p>Teléfono: (+57) "
    "3175073040</p><p>Correo electrónico:  info@ritenterprise.com.co</p><p>Página web: "
    "www.ritenterprise.com.co</p><h2>1. NORMATIVIDAD LEGAL Y ÁMBITO DE APLICACIÓN:</h2><p>La "
    "presente política de Tratamiento de datos personales es elaborada de conformidad con lo "
    "dispuesto en la Constitución Política, la Ley 1581 de 2012, el Decreto Reglamentario "
    "1377 de 2013 y demás disposiciones complementarias y será aplicada por RIT ENTERPRISE "
    "SOLUTIONS SAS, respecto de la recolección, almacenamiento, uso, circulación, supresión "
    "y de todas aquellas actividades que constituyan tratamiento de datos "
    "personales.</p><h2>2. DEFINICIONES:</h2><p>Para efectos de la ejecución de la presente "
    "política y de conformidad con la normatividad legal, serán aplicables las siguientes "
    "definiciones:</p><ul><li>a) Autorización: Consentimiento previo, expreso e informado "
    "del Titular para llevar a cabo el Tratamiento de datos personales;</li><li>b) Aviso de "
    "privacidad: Documento físico, electrónico o en cualquier otro formato generado por el "
    "Responsable que se pone a disposición del Titular para el tratamiento de sus datos "
    "personales. En el Aviso de Privacidad se comunica al Titular la información relativa a "
    "la existencia de las políticas de tratamiento de información que le serán aplicables, "
    "la forma de acceder a las mismas y la finalidad del tratamiento que se pretende dar a "
    "los datos personales;</li><li>c) Base de Datos: Conjunto organizado de datos personales "
    "que sea objeto de Tratamiento;</li><li>d) Dato personal: Cualquier información "
    "vinculada o que pueda asociarse a una o varias personas naturales determinadas o "
    "determinables;</li><li>e) Dato público: Es el dato calificado como tal según los "
    "mandatos de la ley o de la Constitución Política y aquel que no sea semiprivado, "
    "privado o sensible. Son públicos, entre otros, los datos relativos al estado civil de "
    "las personas, a su profesión u oficio, a su calidad de comerciante o de servidor "
    "público y aquellos que puedan obtenerse sin reserva alguna. Por su naturaleza, los "
    "datos públicos pueden estar contenidos, entre otros, en registros públicos, documentos "
    "públicos, gacetas y boletines oficiales;</li><li>f) Dato privado: Es el dato que por su "
    "naturaleza íntima o reservada sólo es relevante para el titular;</li><li>g) Datos "
    "sensibles: Se entiende por datos sensibles aquellos que afectan la intimidad del "
    "Titular o cuyo uso indebido puede generar su discriminación, tales como aquellos que "
    "revelen el origen racial o étnico, la orientación política, las convicciones religiosas "
    "o filosóficas, la pertenencia a sindicatos, organizaciones sociales, de derechos "
    "humanos o que promueva intereses de cualquier partido político o que garanticen los "
    "derechos y garantías de partidos políticos de oposición, así como los datos relativos a "
    "la salud, a la vida sexual y los datos biométricos;</li><li>h) Encargado del "
    "Tratamiento: Persona natural o jurídica, pública o privada, que por sí misma o en "
    "asocio con otros, realice el Tratamiento de datos personales por cuenta del Responsable "
    "del Tratamiento;</li><li>i) Responsable del Tratamiento: Persona natural o jurídica, "
    "pública o privada, que por sí misma o en asocio con otros, decida sobre la base de "
    "datos y/o el Tratamiento de los datos;</li><li>j) Titular: Persona natural cuyos datos "
    "personales sean objeto de Tratamiento;</li><li>k) Tratamiento: Cualquier operación o "
    "conjunto de operaciones sobre datos personales, tales como la recolección, "
    "almacenamiento, uso, circulación o supresión de los mismos.</li></ul><h2>3. FINALIDAD "
    "CON LA QUE SE EFECTÚA LA RECOLECCIÓN DE DATOS PERSONALES Y TRATAMIENTO DE LOS "
    "MISMOS:</h2><p>RIT ENTERPRISE SOLUTIONS SAS podrá hacer uso de los datos personales "
    "para:</p><ul><li>a) Ejecutar la relación contractual existente con sus clientes, "
    "proveedores y trabajadores, incluida el pago de obligaciones contractuales;</li><li>b) "
    "Proveer los servicios y/o los productos requeridos por sus usuarios;</li><li>c) "
    "Informar sobre nuevos productos o servicios y/o sobre cambios en los mismos;</li><li>d) "
    "Evaluar la calidad del servicio;</li><li>e) Realizar estudios internos sobre hábitos de "
    "consumo;</li><li>f) Enviar al correo físico, electrónico, celular o dispositivo móvil, "
    "vía mensajes de texto (SMS y/o MMS) o a través de cualquier otro medio análogo y/o "
    "digital de comunicación creado o por crearse, información comercial, publicitaria o "
    "promocional sobre los productos y/o servicios, eventos y/o promociones de tipo "
    "comercial o no de estas, con el fin de impulsar, invitar, dirigir, ejecutar, informar y "
    "de manera general, llevar a cabo campañas, promociones o concursos de carácter "
    "comercial o publicitario, adelantados por RIT ENTERPRISE SOLUTIONS SAS y/o por terceras "
    "personas;</li><li>g) Desarrollar el proceso de selección, evaluación, y vinculación "
    "laboral;</li><li>h) Soportar procesos de auditoría interna o externa;</li><li>i) "
    "Registrar la información de empleados y/o pensionados (activos e inactivos) en las "
    "bases de datos de RIT ENTERPRISE SOLUTIONS SAS;</li><li>j) Los indicados en la "
    "autorización otorgada por el titular del dato o descritos en el aviso de privacidad "
    "respectivo, según sea el caso;</li><li>k) Suministrar, compartir, enviar o entregar sus "
    "datos personales a empresas filiales, vinculadas, o subordinadas de RIT ENTERPRISE "
    "SOLUTIONS SAS ubicadas en Colombia o cualquier otro país en el evento que dichas "
    "compañías requieran la información para los fines aquí indicados.</li><li>l) Respecto "
    "de los datos (i) recolectados directamente en los puntos de seguridad, (ii) tomados de "
    "los documentos que suministran las personas al personal de seguridad y (iii) obtenidos "
    "de las videograbaciones que se realizan dentro o fuera de las instalaciones de RIT "
    "ENTERPRISE SOLUTIONS SAS, éstos se utilizarán para fines de seguridad de las personas, "
    "los bienes e instalaciones de RIT ENTERPRISE SOLUTIONS SAS y podrán ser utilizados como "
    "prueba en cualquier tipo de proceso.</li><li>m) Si un dato personal es proporcionado, "
    "dicha información será utilizada sólo para los propósitos aquí señalados, y por tanto, "
    "RIT ENTERPRISE SOLUTIONS SAS no procederá a vender, licenciar, transmitir, o divulgar "
    "la misma, salvo que: (i) exista autorización expresa para hacerlo; (ii) sea necesario "
    "para permitir a los contratistas o agentes prestar los servicios encomendados; (iii) "
    "sea necesario con el fin de proveer nuestros servicios y/o productos; (iv) sea "
    "necesario divulgarla a las entidades que prestan servicios de mercadeo en nombre de RIT "
    "ENTERPRISE SOLUTIONS SAS o a otras entidades con las cuales se tengan acuerdos de "
    "mercado conjunto; (v) la información tenga relación con una fusión, consolidación, "
    "adquisición, desinversión, u otro proceso de restructuración de la sociedad; (vi) que "
    "sea requerido o permitido por la ley.</li><li>n) RIT ENTERPRISE SOLUTIONS SAS podrá "
    "subcontratar a terceros para el procesamiento de determinadas funciones o información. "
    "Cuando efectivamente se subcontrate con terceros el procesamiento de información "
    "personal o se proporcione información personal a terceros prestadores de servicios, RIT "
    "ENTERPRISE SOLUTIONS SAS advierte a dichos terceros sobre la necesidad de proteger "
    "dicha información personal con medidas de seguridad apropiadas, se prohíbe el uso de la "
    "información para fines propios y se solicita que no se divulgue la información personal "
    "a otros.</li></ul><h2>4. PRINCIPIOS APLICABLES AL TRATAMIENTO DE DATOS "
    "PERSONALES:</h2><p>El tratamiento de datos personales en RIT ENTERPRISE SOLUTIONS SAS "
    "se regirá por los siguientes principios:</p><ul><li>a) Principio de finalidad: El "
    "Tratamiento de los datos personales recogidos debe obedecer a una finalidad legítima, "
    "la cual debe ser informada al Titular;</li><li>b) Principio de libertad: El Tratamiento "
    "sólo puede llevarse a cabo con el consentimiento, previo, expreso e informado del "
    "Titular. Los datos personales no podrán ser obtenidos o divulgados sin previa "
    "autorización, o en ausencia de mandato legal o judicial que releve el "
    "consentimiento;</li><li>c) Principio de veracidad o calidad: La información sujeta a "
    "Tratamiento debe ser veraz, completa, exacta, actualizada, comprobable y comprensible. "
    "No será efectuado el Tratamiento de datos parciales, incompletos, fraccionados o que "
    "induzcan a error;</li><li>d) Principio de transparencia: En el Tratamiento debe "
    "garantizarse el derecho del Titular a obtener de RIT ENTERPRISE SOLUTIONS SAS en "
    "cualquier momento y sin restricciones, información acerca de la existencia de datos que "
    "le conciernan;</li><li>e) Principio de acceso y circulación restringida: El Tratamiento "
    "se sujeta a los límites que se derivan de la naturaleza de los datos personales, de las "
    "disposiciones de la presente ley y la Constitución. Los datos personales, salvo la "
    "información pública, y lo dispuesto en la autorización otorgada por el titular del "
    "dato, no podrán estar disponibles en Internet u otros medios de divulgación o "
    "comunicación masiva, salvo que el acceso sea técnicamente controlable para brindar un "
    "conocimiento restringido sólo a los Titulares o terceros autorizados;</li><li>f) "
    "Principio de seguridad: La información sujeta a Tratamiento por parte de RIT ENTERPRISE "
    "SOLUTIONS SAS se deberá proteger mediante el uso de las medidas técnicas, humanas y "
    "administrativas que sean necesarias para otorgar seguridad a los registros evitando su "
    "adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento;</li><li>g) "
    "Principio de confidencialidad: Todas las personas que intervengan en el Tratamiento de "
    "datos personales están obligadas a garantizar la reserva de la información, inclusive "
    "después de finalizada su relación con alguna de las labores que comprende el "
    "Tratamiento.</li></ul><p>PARÁGRAFO PRIMERO En el evento que se recolecten datos "
    "personales sensibles, el Titular podrá negarse a autorizar su Tratamiento.</p><h2>5. "
    "DERECHOS DE LOS TITULARES DE DATOS PERSONALES OBJETO DE TRATAMIENTO POR PARTE DE RIT "
    "ENTERPRISE SOLUTIONS SAS:</h2><p>Los titulares de datos personales por sí o por "
    "intermedio de su representante y/o apoderado o su causahabiente podrán ejercer los "
    "siguientes derechos, respecto de los datos personales que sean objeto de tratamiento "
    "por parte de RIT ENTERPRISE SOLUTIONS SAS:</p><ul><li>a) Derecho de acceso: En virtud "
    "del cual podrá acceder a los datos personales que estén bajo el control de RIT "
    "ENTERPRISE SOLUTIONS SAS, para efectos de consultarlos de manera gratuita al menos una "
    "vez cada mes calendario, y cada vez que existan modificaciones sustanciales de las "
    "Políticas de Tratamiento de la información que motiven nuevas consultas;</li><li>b) "
    "Derecho de actualización, rectificación y supresión: En virtud del cual podrá solicitar "
    "la actualización, rectificación y/o supresión de los datos personales objeto de "
    "tratamiento, de tal manera que se satisfagan los propósitos del tratamiento;</li><li>c) "
    "Derecho a solicitar prueba de la autorización: salvo en los eventos en los cuales, "
    "según las normas legales vigentes, no se requiera de la autorización para realizar el "
    "tratamiento;</li><li>d) Derecho a ser informado respecto del uso del dato "
    "personal;</li><li>e) Derecho a presentar quejas ante la Superintendencia de Industria y "
    "Comercio: por infracciones a lo dispuesto en la normatividad vigente sobre tratamiento "
    "de datos personales;</li><li>f) Derecho a requerir el cumplimiento de las órdenes "
    "emitidas por la Superintendencia de Industria y Comercio.</li></ul><p>PARÁGRAFO "
    "PRIMERO: Para efectos del ejercicio de los derechos antes descritos tanto el titular "
    "como la persona que lo represente deberá demostrar su identidad y, de ser el caso, la "
    "calidad en virtud de la cual representa al titular.</p><p>PARÁGRAFO SEGUNDO: Los "
    "derechos de los menores de edad serán ejercidos por medio de las personas que estén "
    "facultadas para representarlos.</p><h2>6. DEBERES DE RIT ENTERPRISE SOLUTIONS "
    "SAS:</h2><p>Todos los obligados a cumplir esta política deben tener presente que RIT "
    "ENTERPRISE SOLUTIONS SAS, está obligada a cumplir los deberes que al respecto imponga "
    "la ley. En consecuencia se deben cumplir las siguientes obligaciones:</p><ul><li>A. "
    "Deberes cuando actúa como responsable: (i) Solicitar y conservar, en las condiciones "
    "previstas en esta política, copia de la respectiva autorización otorgada por el "
    "titular. (ii) Informar de manera clara y suficiente al titular sobre la finalidad de la "
    "recolección y los derechos que le asisten por virtud de la autorización otorgada. (iii) "
    "Informar a solicitud del titular sobre el uso dado a sus datos personales. (iv) "
    "Tramitar las consultas y reclamos formulados en los términos señalados en la presente "
    "política. (v) Procurar que los principios de veracidad, calidad, seguridad y "
    "confidencialidad en los términos establecidos en la siguiente política. (vi) Conservar "
    "la información bajo las condiciones de seguridad necesarias para impedir su "
    "adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento. (vii) "
    "Actualizar la información cuando sea necesario. (viii) Rectificar los datos personales "
    "cuando ello sea procedente.</li><li>B. Deberes cuando obra como Encargado del "
    "tratamiento de datos personales. Si realiza el tratamiento de datos en nombre de otra "
    "entidad u organización (Responsable del tratamiento) deberá cumplir los siguientes "
    "deberes: (i) Establecer que el Responsable del tratamiento esté autorizado para "
    "suministrar los datos personales que tratará como Encargado. (ii) Garantizar al "
    "titular, en todo tiempo, el pleno y efectivo ejercicio del derecho de hábeas data. "
    "(iii)  Conservar la información bajo las condiciones de seguridad necesarias para "
    "impedir su adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento. "
    "(iv) Realizar oportunamente la actualización, rectificación o supresión de los datos. "
    "(v) Actualizar la información reportada por los Responsables del tratamiento dentro de "
    "los cinco (5) días hábiles contados a partir de su recibo. (vi) Tramitar las consultas "
    "y los reclamos formulados por los titulares en los términos señalados en la presente "
    "política. (vii) Registrar en la base de datos la leyenda “reclamo en trámite” en la "
    "forma en que se establece en la presente política. (ix) Insertar en la base de datos la "
    "leyenda “información en discusión judicial” una vez notificado por parte de la "
    "autoridad competente sobre procesos judiciales relacionados con la calidad del dato "
    "personal. (x) Abstenerse de circular información que esté siendo controvertida por el "
    "titular y cuyo bloqueo haya sido ordenado por la Superintendencia de Industria y "
    "Comercio. (xi) Permitir el acceso a la información únicamente a las personas "
    "autorizadas por el titular o facultadas por la ley para dicho efecto. (xii) Informar a "
    "la Superintendencia de Industria y Comercio cuando se presenten violaciones a los "
    "códigos de seguridad y existan riesgos en la administración de la información de los "
    "titulares. (xiii) Cumplir las instrucciones y requerimientos que imparta la "
    "Superintendencia de Industria y Comercio.</li><li>C. Deberes cuando realiza el "
    "tratamiento a través de un Encargado: (i) Suministrar al Encargado del tratamiento "
    "únicamente los datos personales cuyo tratamiento esté previamente autorizado. Para "
    "efectos de la transmisión nacional o internacional de los datos se deberá suscribir un "
    "contrato de transmisión de datos personales o pactar cláusulas contractuales según lo "
    "establecido en el artículo 25 del decreto 1377 de 2013. (ii) Garantizar que la "
    "información que se suministre al Encargado del tratamiento sea veraz, completa, exacta, "
    "actualizada, comprobable y comprensible. (iii) Comunicar de forma oportuna al Encargado "
    "del tratamiento todas las novedades respecto de los datos que previamente le haya "
    "suministrado y adoptar las demás medidas necesarias para que la información "
    "suministrada a este se mantenga actualizada. (iv) Informar de manera oportuna al "
    "Encargado del tratamiento las rectificaciones realizadas sobre los datos personales "
    "para que éste proceda a realizar los ajustes pertinentes. (v) Exigir al Encargado del "
    "tratamiento, en todo momento, el respeto a las condiciones de seguridad y privacidad de "
    "la información del titular. (vi) Informar al Encargado del tratamiento cuando "
    "determinada información se encuentre en discusión por parte del titular, una vez se "
    "haya presentado la reclamación y no haya finalizado el trámite respectivo.</li><li>D. "
    "Deberes respecto de la Superintendencia de Industria y Comercio: (i) Informarle las "
    "eventuales violaciones a los códigos de seguridad y la existencia de riesgos en la "
    "administración de la información de los titulares. (ii) Cumplir las instrucciones y "
    "requerimientos que imparta la Superintendencia de Industria y Comercio.</li></ul><h2>7. "
    "SOLICITUD DE AUTORIZACIÓN AL TITULAR DEL DATO PERSONAL:</h2><p>Con antelación y/o al "
    "momento de efectuar la recolección del dato personal, RIT ENTERPRISE SOLUTIONS SAS "
    "solicitará al titular del dato su autorización para efectuar su recolección y "
    "tratamiento, indicando la finalidad para la cual se solicita el dato, utilizando para "
    "esos efectos medios técnicos automatizados, escritos u orales, que permitan conservar "
    "prueba de la autorización y/o de la conducta inequívoca descrita en el artículo 7 del "
    "Decreto 1377 de 2013. Dicha autorización se solicitará por el tiempo que sea razonable "
    "y necesario para satisfacer las necesidades que dieron origen a la solicitud del dato "
    "y, en todo caso, con observancia de las disposiciones legales que rigen sobre la "
    "materia.</p><h2>8. AVISO DE PRIVACIDAD:</h2><p>En el evento en el que RIT ENTERPRISE "
    "SOLUTIONS SAS no pueda poner a disposición del titular del dato personal la presente "
    "política de tratamiento de la información, publicará el aviso de privacidad que se "
    "adjunta al presente documento, cuyo texto conservará para consulta posterior por parte "
    "del titular del dato y/o de la Superintendencia de Industria y Comercio.</p><h2>9. "
    "LIMITACIONES TEMPORALES AL TRATAMIENTO DE LOS DATOS PERSONALES.</h2><p>RIT ENTERPRISE "
    "SOLUTIONS SAS solo podrá recolectar, almacenar, usar o circular los datos personales "
    "durante el tiempo que sea razonable y necesario, de acuerdo con las finalidades que "
    "justificaron el tratamiento, atendiendo a las disposiciones aplicables a la materia de "
    "que se trate y a los aspectos administrativos, contables, fiscales, jurídicos e "
    "históricos de la información. Una vez cumplida la o las finalidades del tratamiento y "
    "sin perjuicio de normas legales que dispongan lo contrario, procederá a la supresión de "
    "los datos personales en su posesión. No obstante lo anterior, los datos personales "
    "deberán ser conservados cuando así se requiera para el cumplimiento de una obligación "
    "legal o contractual.</p><h2>10. ÁREA RESPONSABLE Y PROCEDIMIENTO PARA EL EJERCICIO DE "
    "LOS DERECHOS DE LOS TITULARES DEL DATO PERSONAL:</h2><p>El ÁREA DE COORDINACION "
    "ADMINISTRATIVA de RIT ENTERPRISE SOLUTIONS SAS será la responsable de atender las "
    "peticiones, quejas y reclamos que formule el titular del dato en ejercicio de los "
    "derechos contemplados en el numeral 5 de la presente política, a excepción del descrito "
    "en su literal e). Para tales efectos, el titular del dato personal o quien ejerza su "
    "representación podrá enviar su petición, queja o reclamo de lunes a viernes de 8:00 a.m "
    "a 5:00 p.m al correo electrónico juan.rojas@ritenterprise.com.co, llamar a la línea "
    "telefónica de RIT ENTERPRISE SOLUTIONS SAS Bogotá (+57) 3175073040, o radicarla en la "
    "siguiente dirección que corresponde a nuestra oficina Av Carrera 9 No. 115-06/30 Ed. "
    "Tierra Firme, Oficina 1207 Bogotá  , a petición, queja o reclamo deberá contener la "
    "identificación del Titular, la descripción de los hechos que dan lugar al reclamo, la "
    "dirección, y acompañando los documentos que se quiera hacer valer. Si el reclamo "
    "resulta incompleto, se requerirá al interesado dentro de los cinco (5) días siguientes "
    "a la recepción del reclamo para que subsane las fallas. Transcurridos dos (2) meses "
    "desde la fecha del requerimiento, sin que el solicitante presente la información "
    "requerida, se entenderá que ha desistido del reclamo. En caso de que quien reciba el "
    "reclamo no sea competente para resolverlo, dará traslado a quien corresponda en un "
    "término máximo de dos (2) días hábiles e informará de la situación al interesado. Una "
    "vez recibido el reclamo completo, se incluirá en la base de datos una leyenda que diga "
    "“reclamo en trámite” y el motivo del mismo, en un término no mayor a dos (2) días "
    "hábiles. Dicha leyenda deberá mantenerse hasta que el reclamo sea decidido. El término "
    "máximo para atender el reclamo será de quince (15) días hábiles contados a partir del "
    "día siguiente a la fecha de su recibo. Cuando no fuere posible atender el reclamo "
    "dentro de dicho término, se informará al interesado los motivos de la demora y la fecha "
    "en que se atenderá su reclamo, la cual en ningún caso podrá superar los ocho (8) días "
    "hábiles siguientes al vencimiento del primer término.</p><h2>11. MEDIDAS DE "
    "SEGURIDAD:</h2><p>En desarrollo del principio de seguridad establecido en la Ley 1581 "
    "de 2012, RIT ENTERPRISE SOLUTIONS SAS adoptará las medidas técnicas, humanas y "
    "administrativas que sean necesarias para otorgar seguridad a los registros evitando su "
    "adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento. El personal "
    "que realice el tratamiento de los datos personales ejecutará los protocolos "
    "establecidos con el fin de garantizar la seguridad de la información.</p><h2>12. FECHA "
    "DE ENTRADA EN VIGENCIA:</h2><p>La presente Política de Datos Personales fue creada el "
    "día 31 de Diciembre de 2015 y entra en vigencia a partir del día 1 de Enero de 2016. "
    "Cualquier cambio que se presente respecto de la presente política, se informará a "
    "través del correo electrónico "
    "info@ritenterprise.com.co</p><p>Atentamente,</p><p>_______________________________________ "
    "JUAN ALVARO ROJAS C.C: 12.991.662 de San Juan (Pasto) Representante Legal Gerente "
    "General</p>"
)


PAGES = [
    {
        "title": "Código de Ética y Buena Conducta",
        "slug": "codigo-etica",
        "codigo": "DE-CO-001",
        "body": BODY_ETICA,
    },
    {
        "title": "Política Sistema Integrado de Gestión SIG",
        "slug": "politica-sig",
        "codigo": "DE-PO-001",
        "body": BODY_SIG,
    },
    {
        "title": "Política de Tratamiento de Datos Personales",
        "slug": "tratamiento-datos",
        "codigo": "DE-PO-004",
        "body": BODY_DATOS,
    },
]

VERSION_DOC = "01"
FECHA_DOC = "30 Abr 26"


def create_politicas(apps, schema_editor):
    from wagtail.models import Page

    from apps.home.models import PoliticaPage, SeccionIndexPage

    home = Page.objects.filter(slug="home").first()
    if home is None:
        return

    index = SeccionIndexPage.objects.filter(slug="politicas").first()
    if index is None:
        index = SeccionIndexPage(title="Políticas", slug="politicas", body=INDEX_BODY)
        home.add_child(instance=index)
        index.save_revision().publish()

    for data in PAGES:
        if PoliticaPage.objects.filter(slug=data["slug"]).exists():
            continue
        page = PoliticaPage(
            title=data["title"],
            slug=data["slug"],
            codigo=data["codigo"],
            version_doc=VERSION_DOC,
            fecha_doc=FECHA_DOC,
            body=data["body"],
        )
        index.add_child(instance=page)
        page.save_revision().publish()


def remove_politicas(apps, schema_editor):
    from apps.home.models import PoliticaPage, SeccionIndexPage

    for data in PAGES:
        PoliticaPage.objects.filter(slug=data["slug"]).delete()
    SeccionIndexPage.objects.filter(slug="politicas").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0022_politicapage"),
        ("wagtailsearch", "0010_add_text_fields"),
    ]

    operations = [
        migrations.RunPython(create_politicas, remove_politicas),
    ]
