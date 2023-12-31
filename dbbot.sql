PGDMP                     	    {            SovDB    15.3    15.3 3    1           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            2           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            3           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            4           1262    19826    SovDB    DATABASE     �   CREATE DATABASE "SovDB" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "SovDB";
                postgres    false            �            1259    19886    applel    TABLE     x   CREATE TABLE public.applel (
    idae integer NOT NULL,
    idap integer,
    pr integer,
    mark character varying
);
    DROP TABLE public.applel;
       public         heap    postgres    false            �            1259    19885    applel_idAe_seq    SEQUENCE     �   CREATE SEQUENCE public."applel_idAe_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."applel_idAe_seq";
       public          postgres    false    225            5           0    0    applel_idAe_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public."applel_idAe_seq" OWNED BY public.applel.idae;
          public          postgres    false    224            �            1259    19872    application    TABLE     �   CREATE TABLE public.application (
    ida integer NOT NULL,
    cath character varying NOT NULL,
    usid integer,
    mincount integer,
    text character varying,
    status character varying
);
    DROP TABLE public.application;
       public         heap    postgres    false            �            1259    19871    application_idA_seq    SEQUENCE     �   CREATE SEQUENCE public."application_idA_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public."application_idA_seq";
       public          postgres    false    223            6           0    0    application_idA_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."application_idA_seq" OWNED BY public.application.ida;
          public          postgres    false    222            �            1259    19846    photo    TABLE     c   CREATE TABLE public.photo (
    idph integer NOT NULL,
    photopath character varying NOT NULL
);
    DROP TABLE public.photo;
       public         heap    postgres    false            �            1259    19845    photo_idPh_seq    SEQUENCE     �   CREATE SEQUENCE public."photo_idPh_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public."photo_idPh_seq";
       public          postgres    false    219            7           0    0    photo_idPh_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public."photo_idPh_seq" OWNED BY public.photo.idph;
          public          postgres    false    218            �            1259    19855    phreq    TABLE     \   CREATE TABLE public.phreq (
    id integer NOT NULL,
    idre integer,
    idpho integer
);
    DROP TABLE public.phreq;
       public         heap    postgres    false            �            1259    19854    phreq_id_seq    SEQUENCE     �   CREATE SEQUENCE public.phreq_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.phreq_id_seq;
       public          postgres    false    221            8           0    0    phreq_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.phreq_id_seq OWNED BY public.phreq.id;
          public          postgres    false    220            �            1259    19837    req    TABLE     �   CREATE TABLE public.req (
    idr integer NOT NULL,
    category character varying NOT NULL,
    description character varying NOT NULL,
    mincount integer
);
    DROP TABLE public.req;
       public         heap    postgres    false            �            1259    19836    req_idR_seq    SEQUENCE     �   CREATE SEQUENCE public."req_idR_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public."req_idR_seq";
       public          postgres    false    217            9           0    0    req_idR_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public."req_idR_seq" OWNED BY public.req.idr;
          public          postgres    false    216            �            1259    19828    users    TABLE     9  CREATE TABLE public.users (
    idnum integer NOT NULL,
    role character varying NOT NULL,
    login character varying NOT NULL,
    name character varying NOT NULL,
    pass character varying NOT NULL,
    email character varying NOT NULL,
    phone character varying NOT NULL,
    tgname character varying
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    19827    users_idNum_seq    SEQUENCE     �   CREATE SEQUENCE public."users_idNum_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."users_idNum_seq";
       public          postgres    false    215            :           0    0    users_idNum_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public."users_idNum_seq" OWNED BY public.users.idnum;
          public          postgres    false    214            �           2604    19889    applel idae    DEFAULT     l   ALTER TABLE ONLY public.applel ALTER COLUMN idae SET DEFAULT nextval('public."applel_idAe_seq"'::regclass);
 :   ALTER TABLE public.applel ALTER COLUMN idae DROP DEFAULT;
       public          postgres    false    225    224    225            �           2604    19875    application ida    DEFAULT     t   ALTER TABLE ONLY public.application ALTER COLUMN ida SET DEFAULT nextval('public."application_idA_seq"'::regclass);
 >   ALTER TABLE public.application ALTER COLUMN ida DROP DEFAULT;
       public          postgres    false    223    222    223            �           2604    19849 
   photo idph    DEFAULT     j   ALTER TABLE ONLY public.photo ALTER COLUMN idph SET DEFAULT nextval('public."photo_idPh_seq"'::regclass);
 9   ALTER TABLE public.photo ALTER COLUMN idph DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    19858    phreq id    DEFAULT     d   ALTER TABLE ONLY public.phreq ALTER COLUMN id SET DEFAULT nextval('public.phreq_id_seq'::regclass);
 7   ALTER TABLE public.phreq ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    221    221                       2604    19840    req idr    DEFAULT     d   ALTER TABLE ONLY public.req ALTER COLUMN idr SET DEFAULT nextval('public."req_idR_seq"'::regclass);
 6   ALTER TABLE public.req ALTER COLUMN idr DROP DEFAULT;
       public          postgres    false    217    216    217            ~           2604    19831    users idnum    DEFAULT     l   ALTER TABLE ONLY public.users ALTER COLUMN idnum SET DEFAULT nextval('public."users_idNum_seq"'::regclass);
 :   ALTER TABLE public.users ALTER COLUMN idnum DROP DEFAULT;
       public          postgres    false    214    215    215            .          0    19886    applel 
   TABLE DATA           6   COPY public.applel (idae, idap, pr, mark) FROM stdin;
    public          postgres    false    225   �6       ,          0    19872    application 
   TABLE DATA           N   COPY public.application (ida, cath, usid, mincount, text, status) FROM stdin;
    public          postgres    false    223   47       (          0    19846    photo 
   TABLE DATA           0   COPY public.photo (idph, photopath) FROM stdin;
    public          postgres    false    219   �7       *          0    19855    phreq 
   TABLE DATA           0   COPY public.phreq (id, idre, idpho) FROM stdin;
    public          postgres    false    221   �9       &          0    19837    req 
   TABLE DATA           C   COPY public.req (idr, category, description, mincount) FROM stdin;
    public          postgres    false    217   �9       $          0    19828    users 
   TABLE DATA           U   COPY public.users (idnum, role, login, name, pass, email, phone, tgname) FROM stdin;
    public          postgres    false    215   x@       ;           0    0    applel_idAe_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."applel_idAe_seq"', 1, false);
          public          postgres    false    224            <           0    0    application_idA_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public."application_idA_seq"', 1, false);
          public          postgres    false    222            =           0    0    photo_idPh_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."photo_idPh_seq"', 1, false);
          public          postgres    false    218            >           0    0    phreq_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.phreq_id_seq', 1, false);
          public          postgres    false    220            ?           0    0    req_idR_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public."req_idR_seq"', 1, false);
          public          postgres    false    216            @           0    0    users_idNum_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."users_idNum_seq"', 1, false);
          public          postgres    false    214            �           2606    19893    applel applel_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.applel
    ADD CONSTRAINT applel_pkey PRIMARY KEY (idae);
 <   ALTER TABLE ONLY public.applel DROP CONSTRAINT applel_pkey;
       public            postgres    false    225            �           2606    19879    application application_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.application
    ADD CONSTRAINT application_pkey PRIMARY KEY (ida);
 F   ALTER TABLE ONLY public.application DROP CONSTRAINT application_pkey;
       public            postgres    false    223            �           2606    19853    photo photo_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.photo
    ADD CONSTRAINT photo_pkey PRIMARY KEY (idph);
 :   ALTER TABLE ONLY public.photo DROP CONSTRAINT photo_pkey;
       public            postgres    false    219            �           2606    19860    phreq phreq_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.phreq
    ADD CONSTRAINT phreq_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.phreq DROP CONSTRAINT phreq_pkey;
       public            postgres    false    221            �           2606    19844    req req_pkey 
   CONSTRAINT     K   ALTER TABLE ONLY public.req
    ADD CONSTRAINT req_pkey PRIMARY KEY (idr);
 6   ALTER TABLE ONLY public.req DROP CONSTRAINT req_pkey;
       public            postgres    false    217            �           2606    19835    users users_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (idnum);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    215            �           2606    19899    applel applel_PR_fkey    FK CONSTRAINT     q   ALTER TABLE ONLY public.applel
    ADD CONSTRAINT "applel_PR_fkey" FOREIGN KEY (pr) REFERENCES public.phreq(id);
 A   ALTER TABLE ONLY public.applel DROP CONSTRAINT "applel_PR_fkey";
       public          postgres    false    221    225    3211            �           2606    19894    applel applel_idAp_fkey    FK CONSTRAINT     |   ALTER TABLE ONLY public.applel
    ADD CONSTRAINT "applel_idAp_fkey" FOREIGN KEY (idap) REFERENCES public.application(ida);
 C   ALTER TABLE ONLY public.applel DROP CONSTRAINT "applel_idAp_fkey";
       public          postgres    false    223    3213    225            �           2606    19880 !   application application_User_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.application
    ADD CONSTRAINT "application_User_fkey" FOREIGN KEY (usid) REFERENCES public.users(idnum);
 M   ALTER TABLE ONLY public.application DROP CONSTRAINT "application_User_fkey";
       public          postgres    false    223    3205    215            �           2606    19866    phreq phreq_idPho_fkey    FK CONSTRAINT     w   ALTER TABLE ONLY public.phreq
    ADD CONSTRAINT "phreq_idPho_fkey" FOREIGN KEY (idpho) REFERENCES public.photo(idph);
 B   ALTER TABLE ONLY public.phreq DROP CONSTRAINT "phreq_idPho_fkey";
       public          postgres    false    3209    221    219            �           2606    19861    phreq phreq_idRe_fkey    FK CONSTRAINT     r   ALTER TABLE ONLY public.phreq
    ADD CONSTRAINT "phreq_idRe_fkey" FOREIGN KEY (idre) REFERENCES public.req(idr);
 A   ALTER TABLE ONLY public.phreq DROP CONSTRAINT "phreq_idRe_fkey";
       public          postgres    false    217    3207    221            .   �   x�uϱB1��g
&@���]�E�!��V0�*�\%���b�&p8b��|����=?��s��<��.�T�9wZ�2
�s�3�$��^r�q/$�R_�;E�����ޫv�ػCa�4ۻ�*�Hc��d��vm������      ,   �   x�����0Dkq�L�kKK�L��E����Wq)�+7
�q�=k�⠸���3t^����^8ˣb�.x�+�\L�w!���Y�n�{�Æ�BL��?�Vk3&o��9%x(>����ʼ�t%�/�+`�      (   �  x���ˎ�@���_�Bհ
���4� �*��g!_�0�q����}� ��=Oi�����N4��+�XSpA�G�0��c��?��|�o���)��]E��q�vs�U������3�  qT�N��a6���uU����n�$��f�wji��>�2bv\��r� �!%ע�SJ��9|H[��_�|��^bt��2�134*}�"Z����ڎ4��B�~��(�Fe�߹d�4��uV�:g�l�!ƺ2�~R�8���i��eE8*��s�*�l�␛���.�y5V?�<��5�}g��uնGO:-ed�Qv]�W'��W���4��!@��oh��`X�7������O�
������ {�3��;�HG�Y��gzkmc����mb[w��� ���G�j.��ap���^n������h���l�I���L&�)"�      *   _   x�ʹ� �Z�`��.��KJ��/����ƕ������Y���x��:�ڙ��.Q(i�Yk��{tܮ�φ���t=I�[q��(>?�
dl      &   j  x��XKr�F\����X�(��m�9A6^f���#Jr������	H��A�w�
9I�� ����bW�0��zz�i�g�t��AzH�Y?6�{�0L��_�^��t�nӈ����س�ߨ�ivk�d��o2��O|��%��!Lc<`�(]�1��u6v���ضs���#X��e�w��Qh݂kK�C�N�a�n�wo�
"�OM~�7�`�o(i���1rW�R�V�9q�#��ܨ�3<̜l���8�qPP1�1���G�&{v�^�H�|�ocv��lY��B�e���B���?F�li�"�6VϘ�#r0��JvW~b_�e��KieS�@�^���6���6��~��V��XƱp�1{�ƭ����ԟ�c�=���#�|Wy�I�Q�Í/<:Zsj�A�ؕ��-�#x��fn��j�m��hZ�}#�K}�c�{+^��;[��uI��DG�� d^D�0Y�!��>>p�{��=b LW%�h�R��Y��5"9��;�J��- ���on��?�D�Sv1J��#Ѳ��m�ɞ�'�T�X��H���n�y�{���TX?,�U��b���P�`6��B�L�Ŝ�m�s��\�����M v:5�,ɔ!F�l���0����|�u,<f��{�&=���&��6�[�(#��&܆e� ~�D�ۭ:&�_%=�>4I������!ߕ�f�/BיxV�Y3��3���D�[��l��8���@La�*��.u��"����d�����z�����9:{Dy�8E;l���l��(t-b��$+# 4��?�@S0v/d,�_��}��)l�G���0i[-m���69�?�=w�[����M�?VØJ$~��:+n�:�@:�hn&g�ğ1���<��F�w����'���&�P���uu:�2ϸ���ږ�&�io��H>�E�M#a�H&:3�B�i9Z�t�F=;Iw�d�!��~l|u�-���T���*TH�rd?G��Z>/�14t2��}�g�g�fÉ��H����dE)�Ǔ�m�?p`��N"���XāI��I[
����Py�|�4vL���b�>մ���J��4,>��ेpH6�ҍt˙1���s�џ��#U��[�g����,�ѴBS٨�
y�� ȗ\ɒ���`�W88�L^Y�mDO��e�Ƈ�m����)�X��͢��W\S��%�1�!4J+�u[�#^	��)a�T@;�ԋ/�*0�e$c]�GDB&�cUx*�,n$&���T����tr��aFl��Q�D3�v]�r6��4�KvN.�	VDj])��wp'!����i��`��}O��kzӕxbt�k�Z`��<�y�E��Im
�{O��c^9s��*j�P�҆/jy:�� ,�+�Zre�͝�`���^�Z0�Hx͞�����g�]/�E�N�.���TmЯyt��N}��pS��Lb����c�	��D�̄8��x}I#�P#��+I�8K&{%N/U�nW�� ��Z�Դ{0���\f�������b����ǳ؅���o�m�3�M��m�)��9��.��	Y�Q
z�懾��L9g��U潏Fʱr���j������3␰��v�_���B���.[��zcD��)t�t��5��b�y����v���=g,      $   n  x����n�@ ���>�ll���-$����*R5��͌�1۩�!�J��=�oP�RJ�<��F��PE=�4��߿� ;s� ��=F}��v���X`��R��	&NL�#�>����N��ݞ��������H�F�J������Vΰ�X�ke�q�4"��	v�l*��d��@�9@��H����ʁ��i�y��S�.��T(�p�a��}�=�Ƕ&�3�J�.B�QY͓�7��?l��J��ݙ3<U��yi��G�d�Te�Qไ�e4�1[��o�o�o��������G~Ͽ�_����?��e��|�������́�vI,YECo$�Q�f4�YLlz��\��h;$,u�"u"�B���R՘�F�˨�&�x�-�]�q
i���D��҂!2j��f;tc�%��m��h�������~e�]��>u�ӳҁ�,�Œ5��+*�Y{�(����ZgF���֝B�%R�ֹ_a~X���36~fG�]� 4&�x�*�c6¬ ˲*AM7�C�t���@��f�߹Mx
������D�\.�W�0��V���I'���m4��b{�tt9X�r63��3�9v�xv!ٔU����㠯�B���!A�     