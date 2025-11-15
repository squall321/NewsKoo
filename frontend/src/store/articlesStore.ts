import { create } from 'zustand';

export type Article = {
  id: string;
  title: string;
  excerpt: string;
  category: string;
  publishedAt: string;
};

type ArticlesState = {
  articles: Article[];
  featuredCategory: string;
  setFeaturedCategory: (category: string) => void;
  addArticle: (article: Article) => void;
};

const initialArticles: Article[] = [
  {
    id: '1',
    title: 'Breaking: Autonomous Newsrooms Take Shape',
    excerpt: 'Media companies explore AI-first newsrooms to speed up fact finding and distribution.',
    category: 'Innovation',
    publishedAt: '2024-02-01',
  },
  {
    id: '2',
    title: 'Audience Habits Shift Toward Personalized Digests',
    excerpt: 'Curated digests tailored to reader intent keep engagement high.',
    category: 'Product',
    publishedAt: '2024-02-04',
  },
  {
    id: '3',
    title: 'How Local Publishers Monetize Newsletters',
    excerpt: 'Small teams leverage sponsorship swaps and memberships to grow revenue.',
    category: 'Business',
    publishedAt: '2024-02-06',
  },
];

export const useArticlesStore = create<ArticlesState>((set) => ({
  articles: initialArticles,
  featuredCategory: 'Innovation',
  setFeaturedCategory: (category) => set({ featuredCategory: category }),
  addArticle: (article) =>
    set((state) => ({
      articles: [...state.articles, article],
    })),
}));
